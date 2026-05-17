<script setup>
/**
 * HomeView component.
 * Displays the main dashboard with search, category filtering, and statistics dashboard.
 */
import { ref, onMounted } from 'vue'
import ResourceList from '../components/ResourceList.vue'
import { resourceService } from '../services/api'

const isLoading = ref(true)
const selectedCategory = ref('All')
const searchQuery = ref('')
const availableCategories = ref(['All'])

const stats = ref({
  total: 0,
  by_category: {},
  by_status: {
    Pending: 0,
    'In Progress': 0,
    Completed: 0
  }
})

/**
 * Fetches current statistics from the API.
 */
const fetchStats = async () => {
  try {
    const response = await resourceService.getStats()
    stats.value = response.data
  } catch (err) {
    console.error('Failed to fetch statistics:', err)
  }
}

onMounted(async () => {
  await fetchStats()
  isLoading.value = false
})

/**
 * Handles the loaded event from ResourceList.
 * Extracts unique categories from the resources and refreshes stats.
 * @param {Array} resources 
 */
const handleResourcesLoaded = async (resources) => {
  const categories = resources.map(r => r.category)
  const uniqueCategories = ['All', ...new Set(categories)]
  availableCategories.value = uniqueCategories
  
  // Refresh stats to ensure dynamic sync
  await fetchStats()
}
</script>

<template>
  <div class="container py-4">
    <!-- Header Section -->
    <div class="row mb-4 align-items-center">
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
            
            <!-- Category Filter & Add CTA -->
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

    <!-- Statistics Section -->
    <div v-if="!isLoading" class="row g-4 mb-5 fade-in">
      <!-- Total Library Card -->
      <div class="col-xl-3 col-md-6">
        <div class="card stat-card border-0 shadow-sm rounded-4 h-100 position-relative overflow-hidden bg-primary-gradient text-white">
          <div class="card-body p-4 d-flex align-items-center justify-content-between">
            <div>
              <span class="text-white-50 text-uppercase small fw-bold">Total Library</span>
              <h2 class="display-6 fw-bold mb-0 mt-1">{{ stats.total }}</h2>
            </div>
            <div class="stat-icon bg-white-20 rounded-circle p-3">
              <i class="bi bi-journal-bookmark-fill fs-3"></i>
            </div>
          </div>
        </div>
      </div>
      
      <!-- Completed Card -->
      <div class="col-xl-3 col-md-6">
        <div class="card stat-card border-0 shadow-sm rounded-4 h-100 bg-white border-start border-4 border-success">
          <div class="card-body p-4 d-flex align-items-center justify-content-between">
            <div>
              <span class="text-secondary text-uppercase small fw-bold">Completed</span>
              <h2 class="display-6 fw-bold mb-0 mt-1 text-success">{{ stats.by_status.Completed || 0 }}</h2>
            </div>
            <div class="stat-icon bg-success-subtle rounded-circle p-3">
              <i class="bi bi-check-circle-fill fs-3 text-success"></i>
            </div>
          </div>
        </div>
      </div>

      <!-- In Progress Card -->
      <div class="col-xl-3 col-md-6">
        <div class="card stat-card border-0 shadow-sm rounded-4 h-100 bg-white border-start border-4 border-warning">
          <div class="card-body p-4 d-flex align-items-center justify-content-between">
            <div>
              <span class="text-secondary text-uppercase small fw-bold">In Progress</span>
              <h2 class="display-6 fw-bold mb-0 mt-1 text-warning">{{ stats.by_status['In Progress'] || 0 }}</h2>
            </div>
            <div class="stat-icon bg-warning-subtle rounded-circle p-3">
              <i class="bi bi-hourglass-split fs-3 text-warning"></i>
            </div>
          </div>
        </div>
      </div>

      <!-- Pending Card -->
      <div class="col-xl-3 col-md-6">
        <div class="card stat-card border-0 shadow-sm rounded-4 h-100 bg-white border-start border-4 border-secondary">
          <div class="card-body p-4 d-flex align-items-center justify-content-between">
            <div>
              <span class="text-secondary text-uppercase small fw-bold">Pending</span>
              <h2 class="display-6 fw-bold mb-0 mt-1 text-secondary">{{ stats.by_status.Pending || 0 }}</h2>
            </div>
            <div class="stat-icon bg-light rounded-circle p-3">
              <i class="bi bi-clock-history fs-3 text-secondary"></i>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Category Breakdown Dashboard -->
    <div v-if="!isLoading && Object.keys(stats.by_category).length > 0" class="card border-0 shadow-sm rounded-4 p-4 bg-white mb-5 fade-in">
      <div class="d-flex align-items-center mb-3">
        <div class="bg-primary-subtle text-primary rounded-circle p-2 me-2" style="width: 32px; height: 32px; display: flex; align-items: center; justify-content: center;">
          <i class="bi bi-tags-fill"></i>
        </div>
        <h5 class="fw-bold text-dark mb-0">Topic Breakdown</h5>
      </div>
      <div class="row g-3">
        <div v-for="(count, category) in stats.by_category" :key="category" class="col-md-3 col-sm-6">
          <div class="p-3 bg-light-gradient border border-light-subtle rounded-4 d-flex justify-content-between align-items-center card-hover-pill">
            <span class="fw-medium text-dark text-truncate pe-2">{{ category }}</span>
            <span class="badge bg-primary-subtle text-primary rounded-pill px-3 py-2 fw-bold">{{ count }}</span>
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
  animation: fadeIn 0.5s ease-in-out;
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

/* Premium Card Designs */
.bg-primary-gradient {
  background: linear-gradient(135deg, #0d6efd 0%, #0a58ca 100%);
}

.bg-white-20 {
  background-color: rgba(255, 255, 255, 0.2);
}

.stat-card {
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.stat-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 10px 20px rgba(0, 0, 0, 0.08) !important;
}

.stat-icon {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 50px;
  height: 50px;
}

.bg-light-gradient {
  background: linear-gradient(180deg, #f8f9fa 0%, #e9ecef 100%);
}

.card-hover-pill {
  transition: all 0.3s ease;
}

.card-hover-pill:hover {
  background: linear-gradient(180deg, #e9ecef 0%, #dee2e6 100%);
  transform: scale(1.02);
  border-color: #0d6efd !important;
}
</style>
