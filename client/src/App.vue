<template>
  <div id="app">
    <link rel="stylesheet" href="//fonts.googleapis.com/css?family=Roboto:300,400,500,700,400italic">
    <link rel="stylesheet" href="//fonts.googleapis.com/icon?family=Material+Icons">

    <md-toolbar>
      <md-button class="md-icon-button" @click="toggleSideBar">
        <md-icon>menu</md-icon>
      </md-button>

      <h1 class="md-title" style="flex: 1">{{ pageName }}</h1>

      <md-button v-if="auth">Logout</md-button>
      <md-button v-else>Login</md-button>
    </md-toolbar>

    <md-sidenav class="md-left" ref="sideBar">
      <md-toolbar class="md-intermediate">
        <div class="md-toolbar-container">
          <h3 class="md-title">Navigation</h3>
        </div>
      </md-toolbar>
      <md-list>
        <md-list-item>
          <md-ink-ripple />
          <md-icon>home</md-icon>
          <span>Home</span>
        </md-list-item>
        <md-list-item>
          <md-ink-ripple />
          <md-icon>explore</md-icon>
          <span>Explore</span>
        </md-list-item>
        <md-divider class="md-dense"></md-divider>
        <md-list-item>
          <md-ink-ripple />
          <md-icon>cloud_upload</md-icon>
          <span>Your Uploads</span>
        </md-list-item>
        <md-list-item>
          <md-ink-ripple />
          <md-icon>forum</md-icon>
          <span>Your Comments</span>
        </md-list-item>
      </md-list>
    </md-sidenav>
    <router-view></router-view>
  </div>
</template>

<script>
export default {
  name: 'app',
  data () {
    return {
      auth: null
    }
  },
  computed: {
    pageName () {
      return this.$store.state.navModule['currentPage']
    }
  },
  methods: {
    toggleSideBar () {
      this.$refs.sideBar.toggle()
    }
  }
}
</script>

<style>
</style>
