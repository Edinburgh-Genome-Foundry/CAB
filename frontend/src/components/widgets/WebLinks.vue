<template lang='pug'>
.weblinks-bar
  a(v-if='tweetMessage', :href='twitterHref') <icon name='twitter' scale='1.5'></icon> Tweet
  a(v-if='emailSubject', :href='emailHref') <icon name='envelope' scale='1.3'></icon> Send feedback
</template>


<script>
export default {
  name: 'web-links',
  props: {
    emailSubject: {default: () => null},
    tweetMessage: {default: () => null},
    tweetUrl: {default: () => ''}
  },
  data: {
  },
  computed: {
    emailHref: function () {
      return ('mailto:egf-software@ed.ac.uk?' +
              '&cc=hille.tekotte@ed.ac.uk, valentin.zulkower@ed.ac.uk' +
              '&body=Hello EGF team !' +
              '&subject=' + this.emailSubject)
    },
    twitterHref: function () {
      return ('https://twitter.com/intent/tweet?' +
              'hashtags=synbio,software' +
              '&text=' + this.tweetMessage +
              '&url=' + this.tweetUrl +
              '&via=EdinGenFoundry')
    }
  }
}
</script>

<style lang='scss' scoped>
.weblinks-bar {
  text-align: center;
  // margin-top: -1em;
  a {
    font-size: 1.2em;
    display: inline-block;
    text-decoration: none;
    color: #888;
    &:not(:first-child) {
      margin-left: 2em;
    }
    &:hover {
      color: black;
    }
  }
  .fa-icon {
    margin-bottom: -.1em;
    margin-right: 0.2em
  }
}
</style>
