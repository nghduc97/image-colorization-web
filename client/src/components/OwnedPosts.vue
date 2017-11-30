<template>
  <section>
    <hero
      title="Owned Posts"
      subtitle="View posts you have posted on the forum."
      >
    </hero>

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
import Hero from './Hero'

export default {
  components: {
    'post-list': PostList,
    'hero': Hero
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
