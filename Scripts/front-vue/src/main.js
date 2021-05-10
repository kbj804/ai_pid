import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import material from './plugins/material'

import VueCookie from 'vue-cookie'

Vue.config.productionTip = false

new Vue({
  router,
  store,
  material,
  VueCookie,


  render: h => h(App),
}).$mount('#app')
