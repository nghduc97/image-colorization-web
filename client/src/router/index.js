import Vue from 'vue'
import Router from 'vue-router'
import Dashboard from '../components/Dashboard'
import Welcome from '../components/Welcome'

Vue.use(Router)

const router = new Router({
  routes: [
    {
      path: '/',
      name: 'Welcome',
      component: Welcome
    },
    {
      path: '/dashboard',
      name: 'Dashboard',
      component: Dashboard
    }
  ]
})

router.beforeEach((to, from, next) => {
  // prevent entering forum without authentication
  if (to.name !== 'Welcome' && !localStorage.getItem('authToken')) {
    next('/')
  } else {
    next()
  }
})

export default router
