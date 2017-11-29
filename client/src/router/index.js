import Vue from 'vue'
import Router from 'vue-router'
import Dashboard from '../components/Dashboard'
import Welcome from '../components/Welcome'
import UserSettings from '../components/UserSettings'
import OwnedPosts from '../components/OwnedPosts'

Vue.use(Router)

const router = new Router({
  mode: 'history',
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
    },
    {
      path: '/settings',
      name: 'Settings',
      component: UserSettings
    },
    {
      path: '/owned',
      name: 'owned',
      component: OwnedPosts
    }
  ]
})

router.beforeEach((to, from, next) => {
  // prevent entering forum without authentication
  if (to.name !== 'Welcome' && !localStorage.getItem('authToken')) {
    next('/')
  } else
  if (to.name === 'Welcome' && localStorage.getItem('authToken')) {
    next('/dashboard')
  } else {
    next()
  }

  // set page title
  document.title = 'ICW - ' + to.name
})

export default router
