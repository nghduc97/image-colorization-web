<template>
  <div class="box">
    <article class="media">
      <div class="media-content">
        <div class="content">
          <p>
            <strong>{{ post['title'] }}</strong> <small>{{ post['time'] }}</small>
            <br>
            {{ post['content'] }}
          </p>

          <a class="button is-primary is-inverted" @click="clap">
            <span>{{ post['total_claps'] + pendingClap }}</span>
            <b-icon icon="sign-language" size="is-small"></b-icon>
          </a>
          <a class="button is-primary is-inverted" @click="showComments">
            <span>Comments</span>
            <b-icon icon="comments" size="is-small"></b-icon>
          </a>
        </div>
      </div>
    </article>
  </div>
</template>

<script>
import PostMixin from './Mixins/PostMixin'

export default {
  mixins: [
    PostMixin
  ]
}
</script>

<style scoped lang="scss">
</style>
