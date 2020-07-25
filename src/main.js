import Vue from 'vue'
import App from './App.vue'
import router from './router'
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
import VueCookies from 'vue-cookies'
import VueI18n from "vue-i18n";

Vue.use(VueI18n)
Vue.use(ElementUI)
Vue.use(VueCookies)
Vue.config.productionTip = false

const i18n = new VueI18n({
  locale:localStorage.getItem('languageSet')||'en',
  messages:{
    'zh':require('@/components/language/zh'),
    'en':require('@/components/language/en')
  }
})

new Vue({
  router,
  i18n,
  render: h => h(App)
}).$mount('#app')
