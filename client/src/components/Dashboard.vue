<template>
  <div>
  </div>
</template>

<script>
import { mapState } from 'vuex'

export default {
  name: 'dashboard',
  mounted () {
    this.$store.commit('nav/changePage', 'Dashboard')
  },
  computed: {
    ...mapState('auth', ['userInfo'])
  }
}
</script>

<style scoped>
</style>
