<template>
  <div class="card">
    <div class="card-image">
      <figure class="image is-1by1" @click="showOriginal ^= true">
        <img class="painted-image" :src="imgUrls.paintedImage">
        <transition name="fade">
          <img class="original-image" v-show="showOriginal" :src="imgUrls.originalImage">
        </transition>
      </figure>
    </div>
    <div class="card-content">
      <div class="media">
        <div class="media-content">
          <div class="content">
            <p class="title is-4">{{ post['title'] }}</p>
            <p class="subtitle is-6">{{ post['time'] }}</p>

            <a class="button is-primary is-inverted" @click="clap">
              <span>{{ post['total_claps'] + pendingClap }}</span>
              <b-icon icon="sign-language" size="is-small"></b-icon>
            </a>
            <a class="button is-primary is-inverted" @click="toDetailPage(post['id'])">
              <span>Comments</span>
              <b-icon icon="comments" size="is-small"></b-icon>
            </a>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { getImageUrls } from '../helpers/image'
import PostMixin from './Mixins/PostMixin'

export default {
  data () {
    return {
      showOriginal: true,
      imgUrls: {}
    }
  },
  created () {
    this.imgUrls = getImageUrls(this.post['id'])
  },
  mixins: [
    PostMixin
  ]
}
</script>

<style scoped lang="scss">
.original-image {
  background-color: gray; // for prototype purpose
}

.painted-image {
  background-color: black; // for prototype purpose
}

.fade-enter-active, .fade-leave-active {
  transition: opacity 0.5s
}
.fade-enter, .fade-leave-to {
  opacity: 0
}
</style>
