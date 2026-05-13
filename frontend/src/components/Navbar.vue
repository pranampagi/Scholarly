<script setup>
/**
 * Navbar component.
 * Provides a responsive Bootstrap navigation bar for the application.
 */
import { RouterLink } from 'vue-router'
</script>

<template>
  <nav class="navbar navbar-expand-lg navbar-dark bg-primary mb-4 shadow-sm">
    <div class="container">
      <router-link class="navbar-brand fw-bold" to="/">
        <span class="bi bi-book-half me-2"></span> Scholarly
      </router-link>
      
      <button 
        class="navbar-toggler" 
        type="button" 
        data-bs-toggle="collapse" 
        data-bs-target="#navbarNav" 
        aria-controls="navbarNav" 
        aria-expanded="false" 
        aria-label="Toggle navigation"
      >
        <span class="navbar-toggler-icon"></span>
      </button>

      <div class="collapse navbar-collapse" id="navbarNav">
        <ul class="navbar-nav ms-auto">
          <li class="nav-item">
            <router-link class="nav-link" active-class="active" to="/">
              Home
            </router-link>
          </li>
          <li class="nav-item">
            <router-link class="nav-link" active-class="active" to="/add">
              Add Resource
            </router-link>
          </li>
        </ul>
      </div>
    </div>
  </nav>
</template>

<style scoped>
.navbar-brand {
  font-size: 1.5rem;
  letter-spacing: 0.5px;
}

.nav-link {
  font-weight: 500;
  transition: color 0.3s ease;
}

.nav-link.active {
  border-bottom: 2px solid white;
}
</style>
