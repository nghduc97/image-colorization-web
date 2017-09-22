<template>
  <div class="posts">
    <image-post
      v-for="(post, idx) in posts"
      :key="idx"
      :post="post">
    </image-post>
  </div>
</template>

<script>
import Axios from 'axios'
import ImagePost from './ImagePost'

export default {
  props: ['api'],
  async mounted () {
    this.posts = await Axios.get(this.api)
  },
  data () {
    return {
      posts: []
    }
  },
  components: {
    'image-post': ImagePost
  }
}
</script>

<style>
  .posts {
    display: flex;
    flex-direction: row;
    min-width: 20em;
    flex-flow: row wrap;
  }
</style>
