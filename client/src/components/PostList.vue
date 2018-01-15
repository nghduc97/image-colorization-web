<template>
  <section>
    <section class="image-post-list" v-if="postType == 1">
      <image-post
        v-for="post in posts"
        :key="post['id']"
        :post="post"
        >
      </image-post>
    </section>
    <section v-if="postType == 2">
      <discuss-post
        v-for="post in posts"
        :key="post['id']"
        :post="post"
        >
      </discuss-post>
    </section>
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
        this.errorMsg('Possible network failure.')
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

@media screen and (min-width: 480px) {
  .image-post-list {
    display: flex;
    flex-wrap: wrap;

    .card {
      width: 360px;
    }
  }
}
</style>
