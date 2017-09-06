import Vue from 'vue'
import Vuex from 'vuex'
import NavModule from './modules/NavModule'

Vue.use(Vuex)

export default new Vuex.Store({
  modules: {
    navModule: NavModule
  },
  strict: true
})
