<template lang="pug">
el-menu(:mode="fullWidth > 610 ? 'horizontal' : 'vertical'" @select="handleSelect", :unique-opened='true')
  .logo(v-if='fullWidth > 610')
    router-link(to='home')
      img(src='../assets/images/CAB-title.png')
  el-menu-item(index='home') Home
  el-submenu(index='2')
    template(slot='title') Scenarios
    //- el-submenu(:index="'2-' + (index + 1)" v-for='(category, index) in scenarios')
    //-     span(slot='title') {{category.category}}
    span(v-for='category in scenarios')
      el-menu-item(v-for='(scenario, subindex) in category.scenarios',
                   :index="scenario.infos.path",
                   :key='scenario.infos.path') {{scenario.infos.navbarTitle}}
  el-menu-item(index='about') About
</template>

<script>
import scenarios from './scenarios/scenarios.js'
export default {
  data: () => ({
    scenarios: scenarios.list,
    fullWidth: 0
  }),
  methods: {
    handleSelect: function (key, keyPath) {
      this.$router.push(key)
    },
    handleResize: function (event) {
      this.fullWidth = document.documentElement.clientWidth
    }
  },
  mounted: function () {
    window.addEventListener('resize', this.handleResize)
    this.handleResize()
  }
}

</script>

<style lang='scss' scoped>
.el-menu, .el-submenu {
  background-color: white;
}

.el-menu {
  border-bottom: 2px solid #dddddd;
}

.logo {
  // display: inline-block;
  float: left;
  margin-left: 20px;
  margin-right: 20px;
  height:60px;
}

.logo img {
  height:140%;
}
</style>
