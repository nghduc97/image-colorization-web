import Vue from 'vue'
import Vuex from 'vuex'
import AuthModule from './modules/AuthModule'

Vue.use(Vuex)

export default new Vuex.Store({
  modules: {
    auth: AuthModule
  },
  strict: process.env.NODE_ENV !== 'production'
})
