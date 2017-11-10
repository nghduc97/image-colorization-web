<template>
  <nav class="navbar" v-if="userInfo">
    <div class="navbar-brand">
        <a class="navbar-item" href="/">
            <img src="/static/Logomakr_3ZFAxR.png">
        </a>
    </div>
    <div class="navbar-menu">
      <div class="navbar-end">
        <div class="navbar-item">
        </div>
      </div>
    </div>
  </nav>
</template>

<script>
import { mapState, mapActions } from 'vuex'

export default {
  methods: {
    ...mapActions({
      logout: 'auth/logout'
    })
  },
  computed: {
    ...mapState('nav', ['currentPage']),
    ...mapState('auth', ['userInfo'])
  }
}
</script>

<style lang="scss">
  .el-header {
    background-color: #B3C0D1;
  }
</style>
