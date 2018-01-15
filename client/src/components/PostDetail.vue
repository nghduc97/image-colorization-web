<template>
  <section>
    <hero
      title="Post Detail"
      subtitle="This is the place to comment on a post."
      >
    </hero>
    <section class="section" v-if="post">
      <h1 class="title">{{ post['title'] }}</h1>
      <div v-if="post['type'] === 1">
        <span>
          <img :src="imgUrls.originalImage">
        </span>
        <span>
          <img :src="imgUrls.paintedImage">
        </span>
      </div>
      <discuss-post
        v-if="post['type'] === 2"
        :post="post">
      </discuss-post>
    </section>
    <section class="section">
      <h1 class="title">Comments</h1>
      <p class="subtitle" v-if="comments.length === 0">No comments yet</p>
      <div v-for="comment in comments" :key="comment['id']">
        <p>
          <strong>{{ comment['user_name'] }}</strong> <small>{{ comment['time'] }}</small>
          <br>
          {{ comment['content'] }}
        </p>
        <hr>
      </div>
      <b-field label="New Comment">
        <b-input
          placeholder="Comment here and hit 'Enter'"
          v-model="newComment"
          @keyup.enter.native="uploadComment"
          autofocus
          id="comment-box"
          >
        </b-input>
      </b-field>
    </section>
  </section>
</template>

<script>
import Axios from 'axios'
import { getImageUrls } from '../helpers/image'
import Hero from './Hero'
import DiscussPost from './DiscussPost'

export default {
  data () {
    return {
      post: null,
      comments: [],
      imgUrls: {},
      newComment: ''
    }
  },
  methods: {
    async uploadComment () {
      try {
        const comment = await Axios.post('/post/comment', {
          'post_id': this.$route.params.postId,
          'content': this.newComment
        })
        this.comments.push(comment)
      } catch (err) {
        this.errorMsg('Failed to upload comment.')
      }
    }
  },
  async mounted () {
    try {
      const cfg = {
        params: {
          'post_id': this.$route.params.postId
        }
      }

      this.post = await Axios.get('/post', cfg)
      this.imgUrls = getImageUrls(this.post['id'])
      this.comments = await Axios.get('/post/comments', cfg)
    } catch (err) {
      this.errorMsg('Possible network failure.')
    }
  },
  components: {
    'discuss-post': DiscussPost,
    'hero': Hero
  }
}
</script>

<style scoped lang="scss">
.section > div {
  margin: auto;
}
</style>
