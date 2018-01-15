import axios from 'axios'
import router from '../../router'

export default {
  namespaced: true,
  state: {
    userInfo: null
  },
  mutations: {
    receiveToken (state, data) {
      localStorage.setItem('authToken', data['token'])
      state.userInfo = data['user_info']
    },
    clearToken (state) {
      localStorage.removeItem('authToken')
      state.userInfo = null
    }
  },
  actions: {
    register (context, registerData) {
      return new Promise(async (resolve, reject) => {
        try {
          const data = await axios.post('/user/register', registerData)
          context.commit('receiveToken', data)
          resolve(context.state['userInfo'])
        } catch (err) {
          reject(err)
        }
      })
    },
    login (context, loginData) {
      return new Promise(async (resolve, reject) => {
        try {
          const data = await axios.post('/user/login', loginData)
          context.commit('receiveToken', data)
          resolve(context.state['userInfo'])
        } catch (err) {
          reject(err)
        }
      })
    },
    logout (context) {
      context.commit('clearToken')
    },
    async verifyToken (context) {
      const token = localStorage.getItem('authToken')
      if (token == null) return

      try {
        const data = await axios.get('/user')
        context.commit('receiveToken', data)
        console.log('Valid token found in local storage')
      } catch (err) {
        console.log('Invalid token found in local storage')
        localStorage.removeItem('authToken')
        router.replace('/')
      }
    }
  }
}
