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
        <a class="navbar-item" @click="logout">
          Logout
        </a>
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

<style lang="scss">
  .el-header {
    background-color: #B3C0D1;
  }
</style>
