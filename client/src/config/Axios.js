import axios from 'axios'

if (process.env.API_HOST) {
  axios.defaults.baseURL = 'http://' + process.env.API_HOST + '/api'
} else {
  axios.defaults.baseURL = '/api'
}

axios.defaults.headers.common['Content-Type'] = 'application/json'
axios.defaults.headers.common['Accept'] = 'application/json'
