import Vue from 'vue'
import Axios from 'axios'

export default Vue.mixin({
  props: {
    post: Object
  },
  data () {
    return {
      pendingClap: 0,
      clapUpload: null
    }
  },
  methods: {
    async uploadClap () {
      await Axios.put('/post/clap', {
        'post_id': this.post['id'],
        'amount': this.pendingClap
      })

      this.post['total_claps'] += this.pendingClap
      this.pendingClap = 0
      this.clapUpload = null
    },
    clap () {
      this.pendingClap++

      // throttle
      if (this.clapUpload) clearTimeout(this.clapUpload)
      this.clapUpload = setTimeout(() => this.uploadClap(), 1000)
    }
  }
})
