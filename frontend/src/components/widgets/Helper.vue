<template lang='pug'>
.helper-div
  el-popover(trigger="hover", :content="help", placement="right", width="220")
    .helper(slot='reference')
</template>
<script>
export default {
  props: {
    help: {default: ''}
  }
}
</script>
<style lang='scss' scoped>
.helper-div {
  display: inline-block;
  .helper:before {
      content: '?';
      display: inline-block;
      font-family: sans-serif;
      font-weight: bold;
      text-align: center;
      margin-left: 10px;
      width: 1em;
      height: 1em;
      font-size: 1em;
      line-height: 1.1em;
      border-radius: 1.2ex;
      margin-right: 4px;
      padding: 1px;
      color: gray;
      background: white;
      border: 1px solid gray;
      text-decoration: none;
  }
}

</style>
