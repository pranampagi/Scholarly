<script setup>
/**
 * HomeView component.
 * Displays the main dashboard and resource list.
 */
import { ref, onMounted } from 'vue'
import ResourceList from '../components/ResourceList.vue'

const isLoading = ref(true)

onMounted(() => {
  // Simulate a brief loading delay for aesthetic effect
  setTimeout(() => {
    isLoading.value = false
  }, 200)
})
</script>

<template>
  <div class="container py-4">
    <!-- Header Section -->
    <div class="row mb-5 align-items-center">
      <div class="col-md-8">
        <h1 class="display-5 fw-bold text-primary mb-2">My Research</h1>
        <p class="lead text-secondary">Organize and track your academic resources effectively.</p>
      </div>
      <div class="col-md-4 text-md-end">
        <router-link to="/add" class="btn btn-primary btn-lg shadow-sm rounded-pill px-4">
          <i class="bi bi-plus-circle me-2"></i>New Resource
        </router-link>
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
      <ResourceList />
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
</style>
