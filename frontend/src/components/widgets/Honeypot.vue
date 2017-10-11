<template lang='pug'>
  input(type='text', size='25', value='', v-model='value')
</template>

<script>
export default {
  props: {
    value: {
      default: () => ''
    }
  },
  data: function () {
    return {
      innervalue: this.value
    }
  },
  watch: {
    value: function (val) {
      this.innervalue = val
    },
    innervalue: function (val) {
      this.$emit('input', val)
    }
  }
}
</script>

<style scoped>
input {
  display: none
}
</style>
