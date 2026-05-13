<script setup>
/**
 * Main application component.
 * Serves as the root of the Vue component tree.
 */
import { RouterView } from 'vue-router'
import Navbar from './components/Navbar.vue'
</script>

<template>
  <div id="app">
    <!-- Main Navigation -->
    <Navbar />

    <!-- Routed Content -->
    <main class="container">
      <RouterView />
    </main>
  </div>
</template>

<style>
/* Global styles */
body {
  background-color: #f8f9fa;
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
}

#app {
  min-height: 100vh;
}
</style>
