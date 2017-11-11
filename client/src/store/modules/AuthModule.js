import axios from 'axios'

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
        console.warn('Invalid token found in local storage')
        console.warn(err)
        localStorage.removeItem('authToken')
      }
    },
    async userInfoChange (context, changeInfo) {
      try {
        const data = await axios.post('/user/info-change', changeInfo)
        context.commit('receiveToken', data)
      } catch (err) {
        console.error(err)
      }
    }
  }
}
