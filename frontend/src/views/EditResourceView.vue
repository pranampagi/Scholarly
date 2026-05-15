<script setup>
/**
 * EditResourceView component.
 * Allows users to update the details of an existing research resource.
 */
import { ref, onMounted } from 'vue'
import { useRouter, useRoute } from 'vue-router'
import { resourceService } from '../services/api'

const router = useRouter()
const route = useRoute()
const resourceId = route.params.id

const formData = ref({
  title: '',
  link: '',
  category: '',
  status: 'Pending'
})

const isLoading = ref(true)
const isSubmitting = ref(false)
const error = ref(null)

/**
 * Fetches the existing resource data on mount.
 */
const fetchResource = async () => {
  try {
    isLoading.value = true
    // Note: We'll use the getAll and filter locally or add a getById if the backend supports it.
    // Our current backend has GET /resources/ (all). 
    // Let's assume we can fetch all and find the one we need for now, 
    // or better, we'll try to call a specific endpoint if we decide to add it.
    // For now, let's fetch all.
    const response = await resourceService.getAll()
    const resource = response.data.find(r => r.id === parseInt(resourceId))
    
    if (resource) {
      formData.value = {
        title: resource.title,
        link: resource.link,
        category: resource.category,
        status: resource.status
      }
    } else {
      error.value = 'Resource not found.'
    }
  } catch (err) {
    console.error('Failed to fetch resource:', err)
    error.value = 'Could not load resource details.'
  } finally {
    isLoading.value = false
  }
}

/**
 * Handles form submission to update the resource.
 */
const handleSubmit = async () => {
  try {
    isSubmitting.value = true
    error.value = null
    await resourceService.update(resourceId, formData.value)
    router.push('/')
  } catch (err) {
    console.error('Failed to update resource:', err)
    error.value = 'Failed to update resource. Please check your connection.'
  } finally {
    isSubmitting.value = false
  }
}

onMounted(fetchResource)
</script>

<template>
  <div class="container py-4">
    <div class="row justify-content-center">
      <div class="col-md-8 col-lg-6">
        <div class="card border-0 shadow-sm rounded-4 overflow-hidden">
          <div class="card-header bg-primary text-white text-center py-4 border-0">
            <h2 class="h4 mb-0 fw-bold">Edit Resource</h2>
          </div>
          
          <div class="card-body p-5">
            <div v-if="isLoading" class="text-center py-4">
              <div class="spinner-border text-primary" role="status"></div>
            </div>

            <template v-else>
              <div v-if="error" class="alert alert-danger mb-4" role="alert">
                <i class="bi bi-exclamation-circle me-2"></i> {{ error }}
              </div>

              <form v-if="!error" @submit.prevent="handleSubmit">
                <!-- Title -->
                <div class="mb-3">
                  <label for="title" class="form-label fw-bold">Resource Title</label>
                  <input 
                    type="text" 
                    class="form-control rounded-pill px-4" 
                    id="title" 
                    v-model="formData.title" 
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
                    Update Resource
                  </button>
                  <router-link to="/" class="btn btn-outline-secondary rounded-pill">
                    Cancel
                  </router-link>
                </div>
              </form>
            </template>
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
