<script setup>
/**
 * AddResourceView component.
 * Provides a form to add new research resources to the database.
 */
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { resourceService } from '../services/api'

const router = useRouter()

const formData = ref({
  title: '',
  link: '',
  category: '',
  status: 'Pending'
})

const isSubmitting = ref(false)
const error = ref(null)

/**
 * Handles form submission.
 */
const handleSubmit = async () => {
  try {
    isSubmitting.value = true
    error.value = null
    await resourceService.create(formData.value)
    router.push('/') // Redirect to dashboard on success
  } catch (err) {
    console.error('Failed to create resource:', err)
    error.value = 'Failed to save resource. Please check your connection.'
  } finally {
    isSubmitting.value = false
  }
}
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
            <div v-if="error" class="alert alert-danger mb-4" role="alert">
              <i class="bi bi-exclamation-circle me-2"></i> {{ error }}
            </div>

            <form @submit.prevent="handleSubmit">
              <!-- Title -->
              <div class="mb-3">
                <label for="title" class="form-label fw-bold">Resource Title</label>
                <input 
                  type="text" 
                  class="form-control rounded-pill px-4" 
                  id="title" 
                  v-model="formData.title" 
                  placeholder="e.g. Attention Is All You Need" 
                  required
                >
              </div>

              <!-- Link -->
              <div class="mb-3">
                <label for="link" class="form-label fw-bold">Link / URL</label>
                <input 
                  type="url" 
                  class="form-control rounded-pill px-4" 
                  id="link" 
                  v-model="formData.link" 
                  placeholder="https://arxiv.org/..." 
                  required
                >
              </div>

              <!-- Category -->
              <div class="mb-3">
                <label for="category" class="form-label fw-bold">Category</label>
                <input 
                  type="text" 
                  class="form-control rounded-pill px-4" 
                  id="category" 
                  v-model="formData.category" 
                  placeholder="e.g. Machine Learning" 
                  required
                >
              </div>

              <!-- Status -->
              <div class="mb-4">
                <label for="status" class="form-label fw-bold">Status</label>
                <select class="form-select rounded-pill px-4" id="status" v-model="formData.status">
                  <option value="Pending">Pending</option>
                  <option value="In Progress">In Progress</option>
                  <option value="Completed">Completed</option>
                </select>
              </div>

              <!-- Actions -->
              <div class="d-grid gap-2">
                <button type="submit" class="btn btn-primary btn-lg rounded-pill px-5" :disabled="isSubmitting">
                  <span v-if="isSubmitting" class="spinner-border spinner-border-sm me-2"></span>
                  Save Resource
                </button>
                <router-link to="/" class="btn btn-outline-secondary rounded-pill">
                  Cancel
                </router-link>
              </div>
            </form>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.form-control:focus, .form-select:focus {
  border-color: #0d6efd;
  box-shadow: 0 0 0 0.25rem rgba(13, 110, 253, 0.1);
}
</style>
