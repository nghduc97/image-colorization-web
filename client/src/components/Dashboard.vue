<template>
  <div>
    <register-form v-if="!userInfo"></register-form>
    <post-list api="/post/top"></post-list>
  </div>
</template>

<script>
import { mapState } from 'vuex'
import RegisterForm from './RegisterForm'
import PostList from './PostList'

export default {
  name: 'dashboard',
  mounted () {
    this.$store.commit('nav/changePage', 'Dashboard')
  },
  computed: {
    ...mapState('auth', ['userInfo'])
  },
  components: {
    'register-form': RegisterForm,
    'post-list': PostList
  }
}
</script>

<style scoped>
</style>
