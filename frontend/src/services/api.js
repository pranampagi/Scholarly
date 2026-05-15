/**
 * API service utility.
 * Centralizes all Axios-based requests to the FastAPI backend.
 */
import axios from 'axios'

const API_BASE_URL = import.meta.env.DEV 
  ? 'http://127.0.0.1:8000' 
  : '/api'

const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json'
  }
})

export const resourceService = {
  /**
   * Fetches all research resources.
   * @returns {Promise}
   */
  getAll() {
    return api.get('/resources/')
  },

  /**
   * Creates a new resource.
   * @param {Object} data 
   * @returns {Promise}
   */
  create(data) {
    return api.post('/resources/', data)
  },

  /**
   * Updates an existing resource.
   * @param {number} id 
   * @param {Object} data 
   * @returns {Promise}
   */
  update(id, data) {
    return api.put(`/resources/${id}`, data)
  },

  /**
   * Deletes a resource.
   * @param {number} id 
   * @returns {Promise}
   */
  delete(id) {
    return api.delete(`/resources/${id}`)
  }
}

export default api
