import axios from 'axios'
import EJSON from 'mongodb-extended-json'

// set API_HOST
if (process.env.API_HOST) {
  axios.defaults.baseURL = 'http://' + process.env.API_HOST + '/api'
} else {
  axios.defaults.baseURL = '/api'
}

// set types for HTTP
axios.defaults.headers.common['Content-Type'] = 'application/json'

// add authToken if available
axios.interceptors.request
  .use(config => {
    const authToken = localStorage.getItem('authToken')
    if (authToken) {
      config.headers['Authorization'] = authToken
    }

    return config
  })

// map response
axios.interceptors.response
  .use(res => {
    const data = EJSON.deserialize(res.data)
    return data
  })
