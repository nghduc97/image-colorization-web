import Axios from 'axios'
import router from '../../router'

export default {
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
      const data = await Axios.put('/post/clap', {
        'post_id': this.post['id'],
        'amount': this.pendingClap
      })

      this.post['total_claps'] += data['amount']
      this.pendingClap = 0
      this.clapUpload = null
    },
    clap () {
      this.pendingClap++

      // throttle
      if (this.clapUpload) clearTimeout(this.clapUpload)
      this.clapUpload = setTimeout(() => this.uploadClap(), 1000)
    },
    toDetailPage (postId) {
      router.push(`/post/${postId}`)
    }
  }
}
