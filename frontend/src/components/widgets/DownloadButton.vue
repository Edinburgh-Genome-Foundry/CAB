<template lang='pug'>
el-button.download.center(type='primary' @click='downloadContent' icon='document') Download Report
</template>

<script>
var download = require('downloadjs')
export default {
  props: {
    button_text: {
      default: 'Submit'
    },
    filedata: {}
  },
  methods: {
    downloadContent: function () {
      // console.log(this.filedata.mimetype, download)
      download(this.filedata.data, this.filedata.name, this.filedata.mimetype)
    }
  }
}
</script>

<style scoped>
</style>
