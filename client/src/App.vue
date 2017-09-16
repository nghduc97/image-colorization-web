<template>
  <div id="app">
    <link rel="stylesheet" href="//fonts.googleapis.com/css?family=Roboto:300,400,500,700,400italic">
    <link rel="stylesheet" href="//fonts.googleapis.com/icon?family=Material+Icons">

    <toolbar ref="toolbar" :sidebarRef="sidebarRef" :auth="auth"></toolbar>
    <sidebar ref="sidebar"></sidebar>
    <router-view></router-view>
  </div>
</template>

<script>
import Toolbar from './components/Toolbar'
import Sidebar from './components/Sidebar'

export default {
  name: 'app',
  mounted () {
    this.sidebarRef = this.$refs.sidebar
  },
  data () {
    return {
      auth: null,
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
</style>
