<template lang="pug">
.file-example

  //- using el-row here because the image and text used to be side by side
  //- and may be so again in the future
  el-row
    el-col.img-column(:xs='24', :sm='24', :lg='24')
      img(v-if='imgSrc', :src='imgSrc')
    el-col.text-column(:xs='24', :sm='24', :lg='24')
      h3
        a(:href='fileHref')
          icon(name='upload' scale='1.3')
          .filename {{dataFilename}}
      p(v-if='description') {{description}}
      slot
  //- hr
</template>

<script>
export default {
  name: 'file-example',
  props: {
    fileHref: {default: ''},
    imgSrc: {default: null},
    description: {default: null},
    filename: {default: null}
  },
  data: function () {
    return {
      defaultImgSrc: null,
      dataFilename: this.filename
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

<style lang='scss' scoped>

.file-example {
  text-align: center;
  hr {
    margin-bottom: 1em;
    border: 0;
    height: 1px;
    background: #333;
    background-image: linear-gradient(to right, #ccc, #333, #ccc);
  }
  .img-column {

    img {
      margin-top: 1em;
      box-shadow: 4px 4px 5px #aaa;
      max-width: 100%;
      max-height: 9em;
    }
  }
  .text-column {
    text-align: left;
    h3 {
      text-align: center;
      .fa-icon {
        margin-bottom: -0.2em;
      }
    }
    a {
      &:hover {

      }

      color: black;
      text-decoration: none;
      .filename {
        display: inline-block;
        margin-left: 0.5em;
      }
    }
  }
}
</style>
