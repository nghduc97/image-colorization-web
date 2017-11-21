<template>
  <section>
    <section class="hero is-primary is-bold">
      <div class="hero-body">
        <div class="container">
          <h1 class="title">
            Dashboard
          </h1>
          <h2 class="subtitle">
            Check out latest and most popular posts on the forum
          </h2>
        </div>
      </div>
    </section>
    <section class="section">
      <h1 class="title">Popular Discusses</h1>
      <hr>
      <discuss-list api-route="/post/top?type=2&sortby=clap"></discuss-list>
    </section>
    <section class="section">
      <h1 class="title">Latest Discusses</h1>
      <hr>
      <discuss-list api-route="/post/top?type=2&sortby=time"></discuss-list>
    </section>
  </section>
</template>

<script>
import { mapState } from 'vuex'
import DiscussList from './DiscussList'

export default {
  name: 'dashboard',
  computed: {
    ...mapState('auth', ['userInfo'])
  },
  components: {
    'discuss-list': DiscussList
  }
}
</script>

<style scoped>
.section {
  padding-bottom: 0;
}
</style>
