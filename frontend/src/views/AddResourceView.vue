<script setup>
/**
 * AddResourceView component.
 * Provides a form to add new research resources.
 */
</script>

<template>
  <div class="container py-4">
    <div class="row justify-content-center">
      <div class="col-md-8 col-lg-6">
        <div class="card border-0 shadow-sm rounded-4 overflow-hidden">
          <div class="card-header bg-primary text-white text-center py-4 border-0">
            <h2 class="h4 mb-0 fw-bold">Add New Resource</h2>
          </div>
          <div class="card-body p-5">
            <div class="text-center mb-4">
              <div class="display-1 text-primary opacity-25 mb-3">
                <i class="bi bi-file-earmark-plus"></i>
              </div>
              <h3 class="h5 text-secondary fw-normal">Resource Form Placeholder</h3>
              <p class="text-muted small">The interactive form will be implemented in the next major update.</p>
            </div>
            
            <div class="d-grid gap-2">
              <router-link to="/" class="btn btn-outline-secondary rounded-pill">
                <i class="bi bi-arrow-left me-2"></i>Back to Library
              </router-link>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.card {
  transition: transform 0.3s ease;
}
.card:hover {
  transform: translateY(-5px);
}
</style>
