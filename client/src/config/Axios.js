import axios from 'axios'
import * as _ from 'lodash'
import { jws } from '../helpers'

// set API_HOST
if (process.env.API_HOST) {
  axios.defaults.baseURL = 'http://' + process.env.API_HOST + '/api'
} else {
  axios.defaults.baseURL = '/api'
}

// set types for HTTP
axios.defaults.headers.common['Content-Type'] = 'application/json'
axios.defaults.headers.common['Accept'] = 'text/plain' // JWS encoded JSON object

// JSON keys' case mapping
const caseMapper = obj => {
  if (obj == null) return null
  if (!_.isObject(obj)) return obj

  const newObj = {}
  for (let key in obj) {
    if (obj.hasOwnProperty(key)) {
      const newKey = _.camelCase(key)
      const value = obj[key]
      newObj[newKey] = caseMapper(value)
    }
  }

  return newObj
}

// add authToken if available
axios.interceptors.request
  .use(config => {
    const authToken = localStorage.getItem('authToken')
    if (authToken) {
      config.headers['Authorization'] = authToken
    }

    return config
  })

// decode from JWS
axios.interceptors.response
  .use(res => {
    const payload = jws.getPayload(res.data)
    return caseMapper(JSON.parse(payload))
  })
