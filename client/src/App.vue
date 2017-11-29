<template>
  <div id="app">
    <toolbar></toolbar>
    <router-view></router-view>
  </div>
</template>

<script>
import Toolbar from './components/Toolbar'

export default {
  name: 'app',
  created () {
    this.$store.dispatch('auth/verifyToken')
  },
  components: {
    'toolbar': Toolbar
  }
}
</script>

<style lang="scss">
// font awesome
$fa-font-path: "~font-awesome/fonts";
@import "~font-awesome/scss/font-awesome";

// bulma config
@import "./color";

@import "~bulma";
@import "~buefy/src/scss/buefy";

// global styles
.input:focus {
  box-shadow: none;
}

textarea {
  resize: none !important;
}

input[type="file"] {
  display: none !important;
}
</style>
