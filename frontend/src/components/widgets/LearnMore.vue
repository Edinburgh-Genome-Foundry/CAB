<template lang="pug">
el-collapse(slot='learnmore-paragr')
  el-collapse-item(title='Learn more', name='1')
    slot Actually there is nothing to learn more
</template>

<style scoped>
.el-collapse {
  border: none;
}

.el-collapse-item__header {
  padding-left: 0px;
}
</style>
