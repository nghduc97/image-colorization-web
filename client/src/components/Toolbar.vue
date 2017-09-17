<template>
  <md-toolbar>
    <md-button class="md-icon-button" @click="toggleSideBar">
      <md-icon>menu</md-icon>
    </md-button>

    <h1 class="md-title" style="flex: 1">{{ pageName }}</h1>

    <md-button v-if="userInfo" @click="logout">Logout</md-button>
    <md-button id="login-button" v-else @click="showLoginDialog">Login</md-button>

    <login-dialog ref="loginDialog"></login-dialog>
  </md-toolbar>
</template>

<script>
import { mapState, mapActions } from 'vuex'
import LoginDialog from './LoginDialog'

export default {
  props: ['sidebarRef'],
  methods: {
    toggleSideBar () {
      this.sidebarRef.toggle()
    },
    showLoginDialog () {
      this.$refs.loginDialog.open()
    },
    ...mapActions({
      logout: 'auth/logout'
    })
  },
  computed: {
    ...mapState('nav', {
      pageName: 'currentPage'
    }),
    ...mapState('auth', {
      userInfo: 'userInfo'
    })
  },
  components: {
    'login-dialog': LoginDialog
  }
}
</script>

<style>
</style>
