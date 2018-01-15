import Vue from 'vue'
import './mixins/ToastMixin'

console.log(process.env)

if (process.env.NODE_ENV === 'production') {
  Vue.config.productionTip = false
}
