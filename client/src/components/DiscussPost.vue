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

          <a>
            {{ post['total_claps'] }}
            <b-icon icon="sign-language" size="is-small"></b-icon>
          </a>
          <a>
            Comments
            <b-icon icon="comments" size="is-small"></b-icon>
          </a>
        </div>
      </div>
    </article>
  </div>
</template>

<script>
export default {
  props: {
    post: Object
  }
}
</script>

<style scoped lang="scss">
</style>
