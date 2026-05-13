<script setup>
/**
 * ResourceList component.
 * Displays a list of research resources in a responsive Bootstrap table.
 * Includes status-based badge styling.
 */
import { ref } from 'vue'

// Mock data for initial development
const resources = ref([
  {
    id: 1,
    title: "Attention Is All You Need",
    link: "https://arxiv.org/abs/1706.03762",
    category: "Machine Learning",
    status: "Completed"
  },
  {
    id: 2,
    title: "Deep Residual Learning for Image Recognition",
    link: "https://arxiv.org/abs/1512.03385",
    category: "Computer Vision",
    status: "In Progress"
  },
  {
    id: 3,
    title: "Innovate to eliminate: a prerequisite in NTD programmes",
    link: "#",
    category: "Public Health",
    status: "Pending"
  }
])

/**
 * Returns the appropriate Bootstrap badge class based on the resource status.
 * @param {string} status 
 * @returns {string}
 */
const getStatusBadgeClass = (status) => {
  switch (status) {
    case 'Completed': return 'bg-success'
    case 'In Progress': return 'bg-warning text-dark'
    case 'Pending': return 'bg-secondary'
    default: return 'bg-light text-dark'
  }
}
</script>

<template>
  <div class="card border-0 shadow-sm rounded-4 overflow-hidden">
    <div class="table-responsive">
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
          <tr v-for="resource in resources" :key="resource.id" class="transition-all">
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
                <button class="btn btn-sm btn-outline-primary rounded-start" title="Edit">
                  <i class="bi bi-pencil"></i>
                </button>
                <button class="btn btn-sm btn-outline-danger rounded-end" title="Delete">
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

.transition-all {
  transition: all 0.2s ease;
}

.badge {
  font-weight: 500;
  font-size: 0.75rem;
}

th {
  letter-spacing: 0.5px;
}
</style>
