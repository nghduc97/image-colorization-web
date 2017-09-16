import axios from 'axios'

export default {
  namespaced: true,
  state: {
    authData: null
  },
  getters: {
    userInfo: state => state.authData ? state.authData['userInfo'] : null
  },
  mutations: {
    receiveToken (state, data) {
      state.authData = data
      axios.defaults.headers.common['Authorization'] = data['token']
      console.log(axios.defaults.headers.common)
    },
    clearToken (state) {
      state.authData = null
      axios.defaults.headers.common['Authorization'] = null
    }
  },
  actions: {
    login (context, data) {
      return new Promise((resolve, reject) => {
        console.log(axios.defaults.headers.common)
        console.log(data)
        axios.post('/user/login', data)
          .then(data => {
            console.log(data)
            context.commit('receiveToken', data)
            resolve(context.getters['userInfo'])
          })
          .catch(err => reject(err))
      })

      // return new Promise((resolve, reject) => {
      //   context.commit('receiveToken', {
      //     'token': '123',
      //     'userInfo': { 'display_name': 'abc' }
      //   })

      //   resolve(context.getters['userInfo'])
      // })
    },
    logout (context) {
      context.commit('clearToken')
    }
  }
}
