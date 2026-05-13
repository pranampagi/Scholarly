<script setup>
/**
 * HomeView component.
 * Displays the main dashboard and resource list.
 */
</script>

<template>
  <div class="container py-4">
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

    <!-- Loading State -->
    <div class="row justify-content-center mt-5">
      <div class="col-md-6 text-center">
        <div class="spinner-border text-primary mb-3" role="status" style="width: 3rem; height: 3rem;">
          <span class="visually-hidden">Loading...</span>
        </div>
        <h4 class="text-muted fw-light">Fetching your research library...</h4>
      </div>
    </div>
  </div>
</template>

<style scoped>
/* Scoped styles for subtle improvements */
h1 {
  letter-spacing: -1px;
}
</style>
