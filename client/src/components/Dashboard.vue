<template>
  <div>
    <register-form v-if="!userInfo"></register-form>
  </div>
</template>

<script>
import { mapState } from 'vuex'
import RegisterForm from './RegisterForm'

export default {
  name: 'dashboard',
  mounted () {
    this.$store.commit('nav/changePage', 'Dashboard')
  },
  computed: {
    ...mapState('auth', {
      userInfo: 'userInfo'
    })
  },
  components: {
    'register-form': RegisterForm
  }
}
</script>

<style scoped>
</style>
