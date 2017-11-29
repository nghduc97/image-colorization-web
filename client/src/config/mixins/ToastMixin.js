import Vue from 'vue'

Vue.mixin({
  methods: {
    errorMsg (msg) {
      this.$toast.open({
        message: msg,
        type: 'is-danger'
      })
    }
  }
})
