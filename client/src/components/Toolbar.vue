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
import { mapGetters, mapActions } from 'vuex'
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
    ...mapGetters({
      pageName: 'nav/pageName',
      userInfo: 'auth/userInfo'
    })
  },
  components: {
    'login-dialog': LoginDialog
  }
}
</script>

<style>
</style>
