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
@import "~bulma/sass/utilities/_all";
$primary: #2196f3;
$primary-invert: findColorInvert($primary);
$accent: #536dfe;
$accent-invert: findColorInvert($accent);

$colors: (
  "white": ($white, $black),
  "black": ($black, $white),
  "light": ($light, $light-invert),
  "dark": ($dark, $dark-invert),
  "primary": ($primary, $primary-invert),
  "accent": ($accent, $accent-invert),
  "info": ($info, $info-invert),
  "success": ($success, $success-invert),
  "warning": ($warning, $warning-invert),
  "danger": ($danger, $danger-invert)
);

$link: $primary;
$link-invert: $primary-invert;
$link-focus-border: $primary;

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
