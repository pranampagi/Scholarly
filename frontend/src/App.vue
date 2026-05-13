<script setup>
/**
 * Main application component.
 * Serves as the root of the Vue component tree.
 */
import { RouterView } from 'vue-router'
</script>

<template>
  <div class="container mt-4">
    <header class="mb-4 text-center">
      <h1 class="display-4 text-primary">Scholarly</h1>
      <nav class="mt-3">
        <router-link to="/" class="btn btn-outline-primary me-2">Home</router-link>
        <router-link to="/add" class="btn btn-outline-primary">Add Resource</router-link>
      </nav>
    </header>

    <main>
      <!-- The component matched by the current route will be rendered here -->
      <RouterView />
    </main>
  </div>
</template>

<style scoped>
/* Basic layout styling */
header {
  border-bottom: 1px solid #dee2e6;
  padding-bottom: 2rem;
}
</style>
