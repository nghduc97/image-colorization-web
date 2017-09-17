<template>
  <div id="app">
    <link rel="stylesheet" href="//fonts.googleapis.com/css?family=Roboto:300,400,500,700,400italic">
    <link rel="stylesheet" href="//fonts.googleapis.com/icon?family=Material+Icons">

    <toolbar ref="toolbar" :sidebarRef="sidebarRef"></toolbar>
    <sidebar ref="sidebar"></sidebar>
    <router-view></router-view>
  </div>
</template>

<script>
import Toolbar from './components/Toolbar'
import Sidebar from './components/Sidebar'

export default {
  name: 'app',
  created () {
    this.$store.dispatch('auth/verifyToken')
  },
  mounted () {
    this.sidebarRef = this.$refs.sidebar
  },
  data () {
    return {
      sidebarRef: this.sidebarRef
    }
  },
  components: {
    'sidebar': Sidebar,
    'toolbar': Toolbar
  }
}
</script>

<style>
  .md-raised {
    box-shadow: none !important;
  }
</style>
