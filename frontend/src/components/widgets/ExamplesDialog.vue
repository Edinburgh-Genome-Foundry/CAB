<template lang="pug">
.examples-dialog
  el-button.examples(type='text', @click='dialogVisible = true') Examples
  el-dialog(title='Examples', :visible.sync='dialogVisible', size='large')
    span This is a message
</template>

<script>
export default {
  props: {},
  data: function () {
    return {
      dialogVisible: false,
      valueMirror: this.value
    }
  },
  methods: {
    change: function (evt) {
      var files = evt.target.files
      var self = this
      self.valueMirror = []
      for (var i = 0; i < files.length; i++) {
        var file = files[i]
        let name = file.name
        if (this.filter(files[i])) {
          var reader = new window.FileReader()
          reader.onloadend = function (ev) {
            if (ev.target.readyState === window.FileReader.DONE) {
              self.valueMirror.push({
                name: name,
                content: ev.target.result
              })
            }
          }
          reader.readAsDataURL(files[i])
        }
      }
    }
  },
  watch: {
    valueMirror: function (val) {
      // this.value = val
      this.$emit('input', this.multiple ? val : val[0])
    }
  }
}
</script>

<style scoped>

.examples {
  font-size: 12px;
  color: rgb(144, 163, 242);
  /*border-radius: 3px;*/
  /*background-color: rgb(241, 240, 249);*/
}
</style>
