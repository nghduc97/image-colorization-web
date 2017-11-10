<template>
  <nav class="navbar" v-if="userInfo">
    <div class="navbar-brand">
      <a class="navbar-item" href="/">
        <img src="/static/Logomakr_3ZFAxR.png">
      </a>
      <div class="navbar-burger burger" @click="menuClasses['is-active'] ^= true">
        <span></span>
        <span></span>
        <span></span>
      </div>
    </div>
    <div v-bind:class="menuClasses">
      <div class="navbar-end">
        <div class="navbar-item has-dropdown is-hoverable">
          <a class="navbar-link">
            {{ userInfo['display_name'] }}
          </a>
          <div class="navbar-dropdown is-right is-boxed">
            <router-link class="navbar-item" to="/">
              My Posts
            </router-link>
            <router-link class="navbar-item" to="/">
              My Comments
            </router-link>
            <hr class="dropdown-divider">
            <router-link class="navbar-item" to="/">
              Settings
            </router-link>
            <a class="navbar-item" @click="logout">
              Logout
            </a>
          </div>
        </div>
      </div>
    </div>
  </nav>
</template>

<script>
import router from '../router'
import { mapState } from 'vuex'

export default {
  data () {
    return {
      menuClasses: {
        'navbar-menu': true,
        'is-active': false
      }
    }
  },
  methods: {
    logout () {
      this.$store.dispatch('auth/logout')
      router.replace('/')
    }
  },
  computed: {
    ...mapState('auth', ['userInfo'])
  }
}
</script>

<style scoped lang="scss">
.navbar-dropdown {
  box-shadow: 0 0 0 1px rgba(10, 10, 10, 0.1) !important;
}
</style>
