<template>
  <section>
    <image-post
      v-for="post in posts"
      v-if="post['type'] == 1"
      :key="post['id']"
      :post="post"
      >
    </image-post>
    <discuss-post
      v-for="post in posts"
      v-if="post['type'] == 2"
      :key="post['id']"
      :post="post"
      >
    </discuss-post>
    <div class="card">
      <footer>
        <a class="card-footer-item button is-primary is-inverted" @click="loadMore">View More</a>
      </footer>
    </div>
  </section>
</template>

<script>
import Axios from 'axios'
import router from '../router'
import DiscussPost from './DiscussPost'
import ImagePost from './ImagePost'

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
    apiRoute: {
      type: String,
      default: '/post/top'
    },
    sortBy: String,
    postType: Number,
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

        this.posts.push(...newPosts)
      } catch (err) {
        this.$toast.open({
          message: 'Possible network failure.',
          type: 'is-danger'
        })
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
    'discuss-post': DiscussPost,
    'image-post': ImagePost
  }
}
</script>

<style scoped lang="scss">
.card {
  max-width: 800px;
  margin-bottom: 1rem;
  margin-left: auto;
  margin-right: auto;
}
</style>
