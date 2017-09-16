<template>
  <md-sidenav class="md-left" ref="sidebar">
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
</template>

<script>
export default {
  name: 'sidebar',
  methods: {
    toggle () {
      this.$refs.sidebar.toggle()
    }
  }
}
</script>

<style>
</style>
