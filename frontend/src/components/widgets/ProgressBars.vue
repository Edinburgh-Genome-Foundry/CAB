<template lang='pug'>
.progress-bars
  p(v-for="bar in order" v-if='bars[bar] && bars[bar].index <= bars[bar].total')
    span {{bars[bar].title}} {{ bars[bar].index }} / {{ bars[bar].total }}
    el-progress(:percentage="100 * bars[bar].index / bars[bar].total", :show-text='false')
</template>


<script>
export default {
  props: {
    bars: {default: () => ({})},
    order: {default: () => ({})}
  }
}
</script>

<style lang='scss' scoped>
.progress-bars {
  font-family: 'Inconsolata', Courier;
}
</style>
