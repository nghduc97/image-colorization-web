import Vue from 'vue'
import Vuex from 'vuex'
import NavModule from './modules/NavModule'
import AuthModule from './modules/AuthModule'

Vue.use(Vuex)

export default new Vuex.Store({
  modules: {
    nav: NavModule,
    auth: AuthModule
  },
  strict: process.env.NODE_ENV !== 'production'
})
