<script setup>
/**
 * ResourceList component.
 * Displays a list of research resources fetched from the backend API.
 */
import { ref, onMounted, computed } from 'vue'
import { resourceService } from '../services/api'

const props = defineProps({
  filterCategory: {
    type: String,
    default: 'All'
  },
  searchQuery: {
    type: String,
    default: ''
  }
})

const emit = defineEmits(['loaded'])

const resources = ref([])
const error = ref(null)
const isLoading = ref(true)

/**
 * Fetches data from the backend.
 */
const fetchResources = async () => {
  try {
    isLoading.value = true
    const response = await resourceService.getAll()
    resources.value = response.data
    emit('loaded', resources.value)
    error.value = null
  } catch (err) {
    console.error('Failed to fetch resources:', err)
    error.value = 'Could not connect to the server. Please ensure the backend is running.'
  } finally {
    isLoading.value = false
  }
}

/**
 * Deletes a resource after user confirmation.
 * @param {number} id 
 */
const deleteResource = async (id) => {
  if (confirm('Are you sure you want to delete this resource?')) {
    try {
      await resourceService.delete(id)
      await fetchResources() // Refresh the list
    } catch (err) {
      alert('Failed to delete resource.')
    }
  }
}

/**
 * Returns the appropriate Bootstrap badge class based on the status.
 */
const getStatusBadgeClass = (status) => {
  switch (status) {
    case 'Completed': return 'bg-success'
    case 'In Progress': return 'bg-warning text-dark'
    case 'Pending': return 'bg-secondary'
    default: return 'bg-light text-dark'
  }
}

/**
 * Computed property to filter resources based on category and search query.
 */
const filteredResources = computed(() => {
  let result = resources.value

  // Apply Category Filter
  if (props.filterCategory && props.filterCategory !== 'All') {
    result = result.filter(r => r.category === props.filterCategory)
  }

  // Apply Search Query Filter (case-insensitive)
  if (props.searchQuery) {
    const query = props.searchQuery.toLowerCase()
    result = result.filter(r => r.title.toLowerCase().includes(query))
  }

  return result
})

onMounted(fetchResources)
</script>

<template>
  <div v-if="error" class="alert alert-danger shadow-sm rounded-4 mb-4" role="alert">
    <i class="bi bi-exclamation-triangle-fill me-2"></i> {{ error }}
    <button @click="fetchResources" class="btn btn-sm btn-outline-danger ms-3">Retry</button>
  </div>

  <div class="card border-0 shadow-sm rounded-4 overflow-hidden">
    <!-- Loading Overlay -->
    <div v-if="isLoading" class="p-5 text-center">
      <div class="spinner-border text-primary" role="status"></div>
    </div>

    <div v-else-if="filteredResources.length === 0" class="p-5 text-center text-muted">
      <i class="bi bi-search display-4 mb-3"></i>
      <p>No resources found in this category.</p>
    </div>

    <div v-else class="table-responsive">
      <table class="table table-hover align-middle mb-0">
        <thead class="bg-light text-secondary small text-uppercase fw-bold">
          <tr>
            <th class="ps-4 py-3">Resource Title</th>
            <th class="py-3">Category</th>
            <th class="py-3">Status</th>
            <th class="py-3 text-end pe-4">Actions</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="resource in filteredResources" :key="resource.id">
            <td class="ps-4 py-3">
              <div class="fw-bold text-dark">{{ resource.title }}</div>
              <a :href="resource.link" target="_blank" class="small text-decoration-none text-primary">
                <i class="bi bi-link-45deg"></i> View Source
              </a>
            </td>
            <td class="py-3">
              <span class="badge bg-info-subtle text-info border border-info-subtle rounded-pill px-3">
                {{ resource.category }}
              </span>
            </td>
            <td class="py-3">
              <span :class="['badge rounded-pill px-3', getStatusBadgeClass(resource.status)]">
                {{ resource.status }}
              </span>
            </td>
            <td class="py-3 text-end pe-4">
              <div class="btn-group">
                <button class="btn btn-sm btn-outline-danger" @click="deleteResource(resource.id)" title="Delete">
                  <i class="bi bi-trash"></i>
                </button>
              </div>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<style scoped>
.table-hover tbody tr:hover {
  background-color: #fbfcfe;
}
.badge {
  font-weight: 500;
  font-size: 0.75rem;
}
</style>
