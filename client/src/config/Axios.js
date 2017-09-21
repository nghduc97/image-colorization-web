import axios from 'axios'
import EJSON from 'mongodb-extended-json'

// set API_HOST
if (process.env.API_HOST) {
  axios.defaults.baseURL = 'http://' + process.env.API_HOST + '/api'
} else {
  axios.defaults.baseURL = '/api'
}

// set types for HTTP
axios.defaults.headers.common['Content-Type'] = 'application/json-extended'

// map request
axios.interceptors.request
  .use(req => {
    // add authToken if available
    const authToken = localStorage.getItem('authToken')
    if (authToken) {
      req.headers['Authorization'] = authToken
    }

    // BSON -> EJSON
    req.data = EJSON.serialize(req.data)

    // return
    return req
  })

// map response
axios.interceptors.response
  .use(res => {
    const data = EJSON.deserialize(res.data)
    return data
  })
