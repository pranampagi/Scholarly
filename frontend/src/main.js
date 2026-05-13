/**
 * Main entry point for the Vue.js frontend.
 * Initializes the Vue app and imports global styles like Bootstrap.
 */
import { createApp } from 'vue'
import './style.css'
import 'bootstrap/dist/css/bootstrap.min.css'
import App from './App.vue'
import router from './router'

const app = createApp(App)
app.use(router)
app.mount('#app')
