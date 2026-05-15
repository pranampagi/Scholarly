/**
 * Router configuration for the Scholarly application.
 * Defines the mapping between URLs and view components.
 */
import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import AddResourceView from '../views/AddResourceView.vue'
import EditResourceView from '../views/EditResourceView.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/add',
    name: 'add-resource',
    component: AddResourceView
  },
  {
    path: '/edit/:id',
    name: 'edit-resource',
    component: EditResourceView
  }
]

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes
})

export default router
