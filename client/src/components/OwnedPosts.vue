<template>
  <section>
    <section class="hero is-primary is-bold">
      <div class="hero-body">
        <div class="container">
          <h1 class="title">
            Owned Posts
          </h1>
          <h2 class="subtitle">
            View posts you have posted on the forum.
          </h2>
        </div>
      </div>
    </section>

    <section class="section">
      <h1 class="title" style="display: inline-block">Image Posts</h1>
      <b-tag class="is-accent is-medium">
        <p>Click on the image to see <strong>Magic</strong></p>
      </b-tag>
      <hr>
      <post-list :post-type="1" :limit="4" api-route="post/owned">
      </post-list>
    </section>

    <section class="section">
      <h1 class="title">Discuss Posts</h1>
      <hr>
      <post-list :post-type="2" api-route="post/owned"></post-list>
    </section>
  </section>
</template>

<script>
import PostList from './PostList'

export default {
  components: {
    'post-list': PostList
  }
}
</script>

<style scoped lang="scss">
.section {
  padding-bottom: 0;
}

@import "../color";
.tag strong {
  color: $white;
}
</style>
