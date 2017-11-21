<template>
  <section>
    <div class="card" v-for="post in discusses" :key="post['id']">
      <header class="card-header">
        <p class="card-header-title">
          {{ post['title'] }}
        </p>
      </header>
      <div class="card-content">
        <div class="content">
          {{ post['content'] }}
        </div>
        <div>
          <a>#tag1</a>
          <a>#tag2</a>
          <br>
          <p>{{ post['time'] }}</p>
        </div>
      </div>
      <footer class="card-footer">
        <a class="card-footer-item">
          {{ post['total_claps'] }} Clap
        </a>
        <a class="card-footer-item">Comment</a>
      </footer>
    </div>
    <div class="card">
      <footer>
          <a class="card-footer-item" @click="loadMore">View More</a>
      </footer>
    </div>
  </section>
</template>

<script>
import Axios from 'axios'
import router from '../router'

export default {
  props: {
    apiRoute: String,
    redirect: String,
    loadMorePosts: {
      type: Function,
      default: function () { console.log('empty method') }
    }
  },
  data () {
    return {
      discusses: []
    }
  },
  methods: {
    async loadDiscusses () {
      try {
        const newPosts = await Axios.get(this.apiRoute)
        console.log(newPosts)

        this.discusses.push(...newPosts)
      } catch (err) {
        console.error(err)
      }
    },
    loadMore () {
      if (this.redirect) {
        router.push(this.redirect)
      } else {
        this.loadMorePosts()
      }
    }
  },
  watch: {
    apiRoute (val) {
      this.loadDiscusses()
    }
  },
  mounted () {
    this.loadDiscusses()
  }
}
</script>

<style scoped lang="scss">
.card {
  margin-bottom: 1rem;
}
</style>
