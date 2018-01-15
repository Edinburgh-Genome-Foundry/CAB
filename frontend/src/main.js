import Vue from 'vue'
import VueRouter from 'vue-router'
import VueResource from 'vue-resource'
import Icon from 'vue-awesome/components/Icon'
import 'vue-awesome/icons'
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
import locale from 'element-ui/lib/locale/lang/en'
import App from './App'
import Home from './components/pages/Home'
import About from './components/pages/About'
import scenarios from './components/scenarios/scenarios'
import widgets from './components/widgets'

// Globally register bootstrap-vue components

Vue.use(VueResource)
Vue.use(VueRouter)
Vue.component('icon', Icon)
Vue.use(ElementUI, { locale })
Vue.use(widgets)

// Check the users auth status when the app starts

const routes = [{
  path: '/home',
  component: Home,
  meta: {title: 'CAB - Home'}
}, {
  path: '/about',
  component: About,
  meta: {title: 'CAB - About'}
}
]

scenarios.list.forEach(function (category) {
  category.scenarios.forEach(function (scenario) {
    console.log(scenario)
    var infos = scenario.default.infos
    routes.push({
      path: '/' + infos.path,
      component: scenario.default,
      meta: {title: 'CAB - ' + infos.title}
    })
  })
})
routes.push({
  path: '*',
  component: Home
})

console.log(routes)

const router = new VueRouter({
  routes,
  mode: 'history'
})
router.beforeEach((to, from, next) => {
  document.title = to.meta.title
  next()
})

/* eslint-disable no-new */
new Vue({
  router,
  el: '#app',
  template: '<App/>',
  components: {
    App
  }
})
