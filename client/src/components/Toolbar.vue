<template>
  <md-toolbar>
    <md-button class="md-icon-button" @click="toggleSideBar">
      <md-icon>menu</md-icon>
    </md-button>

    <h1 class="md-title" style="flex: 1">{{ pageName }}</h1>

    <md-button v-if="auth">Logout</md-button>
    <md-button v-else>Login</md-button>
  </md-toolbar>
</template>

<script>
export default {
  props: ['auth', 'sidebarRef'],
  methods: {
    toggleSideBar () {
      this.sidebarRef.toggle()
    }
  },
  computed: {
    pageName () {
      return this.$store.state.navModule['currentPage']
    }
  }
}
</script>

<style>
</style>
