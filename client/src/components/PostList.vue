<template>
  <section>
    <discuss-post
      v-for="post in posts"
      v-if="post['type'] == 2"
      :key="post['id']"
      :post="post"
      >
    </discuss-post>
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
import DiscussPost from './DiscussPost'

export default {
  props: {
    owned: {
      type: Number,
      default: 0
    },
    limit: {
      type: Number,
      default: 5
    },
    offset: {
      type: Number,
      default: 0
    },
    sortBy: String,
    postType: Number,
    apiRoute: String,
    redirect: String
  },
  data () {
    return {
      posts: [],
      currentOffset: this.offset
    }
  },
  methods: {
    async loadPosts () {
      try {
        const newPosts = await Axios.get(this.apiRoute, {
          params: {
            'sortby': this.sortBy,
            'type': this.postType,
            'offset': this.currentOffset,
            'limit': this.limit
          }
        })
        console.log(newPosts)

        this.posts.push(...newPosts)
      } catch (err) {
        console.error(err)
      }
    },
    loadMore () {
      if (this.redirect) {
        router.push(this.redirect)
      } else {
        this.currentOffset += this.limit
        this.loadPosts()
      }
    }
  },
  mounted () {
    this.loadPosts()
  },
  components: {
    'discuss-post': DiscussPost
  }
}
</script>

<style scoped lang="scss">
.card {
  margin-bottom: 1rem;
}
</style>
