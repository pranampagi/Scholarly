<script setup>
/**
 * HomeView component.
 * Displays the main dashboard with search and category filtering.
 */
import { ref, onMounted } from 'vue'
import ResourceList from '../components/ResourceList.vue'

const isLoading = ref(true)
const selectedCategory = ref('All')
const searchQuery = ref('')
const availableCategories = ref(['All'])

onMounted(() => {
  // Simulate a brief loading delay for aesthetic effect
  setTimeout(() => {
    isLoading.value = false
  }, 200)
})

/**
 * Handles the loaded event from ResourceList.
 * Extracts unique categories from the resources.
 * @param {Array} resources 
 */
const handleResourcesLoaded = (resources) => {
  const categories = resources.map(r => r.category)
  const uniqueCategories = ['All', ...new Set(categories)]
  availableCategories.value = uniqueCategories
}
</script>

<template>
  <div class="container py-4">
    <!-- Header Section -->
    <div class="row mb-5 align-items-center">
      <div class="col-lg-6 mb-4 mb-lg-0">
        <h1 class="display-5 fw-bold text-primary mb-2">My Research</h1>
        <p class="lead text-secondary">Organize and track your academic resources effectively.</p>
      </div>
      
      <div class="col-lg-6">
        <div class="card border-0 shadow-sm rounded-4 p-3 bg-white">
          <div class="row g-3">
            <!-- Search Input -->
            <div class="col-md-7">
              <div class="input-group">
                <span class="input-group-text bg-white border-end-0 rounded-start-pill ps-3">
                  <i class="bi bi-search text-muted"></i>
                </span>
                <input 
                  type="text" 
                  v-model="searchQuery" 
                  class="form-control border-start-0 rounded-end-pill px-3" 
                  placeholder="Search resources by title..."
                >
              </div>
            </div>
            
            <!-- Category Filter -->
            <div class="col-md-5 d-flex gap-2">
              <select v-model="selectedCategory" class="form-select shadow-none rounded-pill px-3">
                <option v-for="cat in availableCategories" :key="cat" :value="cat">
                  {{ cat }}
                </option>
              </select>
              <router-link to="/add" class="btn btn-primary rounded-circle shadow-sm flex-shrink-0" title="Add New Resource" style="width: 38px; height: 38px; padding: 0; display: flex; align-items: center; justify-content: center;">
                <i class="bi bi-plus-lg"></i>
              </router-link>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Content Section -->
    <div v-if="isLoading" class="row justify-content-center mt-5 py-5">
      <div class="col-md-6 text-center">
        <div class="spinner-border text-primary mb-3" role="status" style="width: 3rem; height: 3rem;">
          <span class="visually-hidden">Loading...</span>
        </div>
        <h4 class="text-muted fw-light">Fetching your research library...</h4>
      </div>
    </div>

    <div v-else class="fade-in">
      <ResourceList 
        :filter-category="selectedCategory" 
        :search-query="searchQuery"
        @loaded="handleResourcesLoaded"
      />
    </div>
  </div>
</template>

<style scoped>
h1 {
  letter-spacing: -1px;
}

.fade-in {
  animation: fadeIn 0.5s ease-in;
}

@keyframes fadeIn {
  from { opacity: 0; transform: translateY(10px); }
  to { opacity: 1; transform: translateY(0); }
}

.input-group-text, .form-control, .form-select {
  border-color: #dee2e6;
}

.form-control:focus, .form-select:focus {
  border-color: #0d6efd;
  box-shadow: none;
}
</style>
