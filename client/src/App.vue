<template>
  <div id="app">
    <toolbar></toolbar>
    <router-view></router-view>
  </div>
</template>

<script>
import Toolbar from './components/Toolbar'

export default {
  name: 'app',
  created () {
    this.$store.dispatch('auth/verifyToken')
  },
  components: {
    'toolbar': Toolbar
  }
}
</script>

<style>
</style>
