import Vue from 'vue'

console.log(process.env)

if (process.env.NODE_ENV === 'production') {
  Vue.config.productionTip = false
}
