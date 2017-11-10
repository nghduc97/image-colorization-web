import axios from 'axios'

// set API_HOST
if (process.env.API_HOST) {
  axios.defaults.baseURL = 'http://' + process.env.API_HOST + '/api'
} else {
  axios.defaults.baseURL = '/api'
}

// set types for HTTP
axios.defaults.headers.common['Content-Type'] = 'application/json'

// map request
axios.interceptors.request
  .use(req => {
    // add authToken if available
    const authToken = 'Bearer ' + localStorage.getItem('authToken')
    if (authToken) {
      req.headers['Authorization'] = authToken
    }

    // return
    return req
  })

// map response
axios.interceptors.response
  .use(res => res.data)
