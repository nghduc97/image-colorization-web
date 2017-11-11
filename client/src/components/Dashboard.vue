<template>
  <div>
  </div>
</template>

<script>
import { mapState } from 'vuex'

export default {
  name: 'dashboard',
  computed: {
    ...mapState('auth', ['userInfo'])
  }
}
</script>

<style scoped>
</style>
