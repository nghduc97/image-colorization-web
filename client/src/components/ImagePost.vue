<template>
  <span class="image-post">
    <md-toolbar class="md-accent">
      <h3 class="md-title">{{ post['title'] }}</h3>
    </md-toolbar>
    <md-card>
      <md-card-media>
        <img :src="'data:image/jpg;base64,' + post['original_image']">
      </md-card-media>
      <md-card-media>
        <img :src="'data:image/jpg;base64,' + post['original_image']">
      </md-card-media>
    </md-card>
  </span>
</template>

<script>
export default {
  props: ['post']
}
</script>

<style lang="scss">
  .image-post {
    margin: 1em 1em;

    .md-card {
      width: 20em;
      height: 40em;

      .md-card-media {
        height: 50%;
        display: flex;
        align-items: center;
        justify-content: center;

        img {
          margin: 0;
        }
      }
    }
  }
</style>
