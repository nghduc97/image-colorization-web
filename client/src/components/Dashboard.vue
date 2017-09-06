<template>
</template>

<script>
export default {
  name: 'dashboard',
  mounted () {
    this.$store.commit('changePage', 'Dashboard')
  }
}
</script>

<style lang="sass" scoped>
</style>
