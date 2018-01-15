<template lang="pug">
.collapsible
  el-collapse
    el-collapse-item(:title='title', name='1')
      slot
</template>

<script>
export default {
  props: {
    title: {default: 'Examples'}
  }
}
</script>

<style lang='scss' scoped>
.collapsible {
  .el-collapse {
    border: none;
  }
  .el-collapse /deep/ {
    .el-collapse-item__header {
      color: rgb(144, 163, 242);

      font-size: 1em;
    }
    i.el-collapse-item__header__arrow {
      display: none !important;
    }
  }
  hr {
    border: 0;
    height: 1px;
    background: #333;
    background-image: linear-gradient(to right, #ccc, #333, #ccc);
  }
}
</style>
