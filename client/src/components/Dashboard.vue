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
      <h1 class="title">Popular Images</h1>
      <hr>
      <post-list :post-type="1" sort-by="clap">
      </post-list>
    </section>

    <section class="section">
      <h1 class="title">Latest Images</h1>
      <hr>
      <post-list :post-type="1" sort-by="time">
      </post-list>
    </section>

    <section class="section">
      <h1 class="title">Popular Discusses</h1>
      <hr>
      <post-list :post-type="2" sort-by="clap">
      </post-list>
    </section>

    <section class="section">
      <h1 class="title">Latest Discusses</h1>
      <hr>
      <post-list :post-type="2" sort-by="time"></post-list>
    </section>
  </section>
</template>

<script>
import { mapState } from 'vuex'
import PostList from './PostList'

export default {
  name: 'dashboard',
  computed: {
    ...mapState('auth', ['userInfo'])
  },
  components: {
    'post-list': PostList
  }
}
</script>

<style scoped>
.section {
  padding-bottom: 0;
}
</style>
