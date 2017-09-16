<template>
</template>

<script>
export default {
  name: 'dashboard',
  mounted () {
    this.$store.commit('nav/changePage', 'Dashboard')
  }
}
</script>

<style lang="sass" scoped>
</style>
