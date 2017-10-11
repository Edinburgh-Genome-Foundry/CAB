<template lang='pug'>
  #app
    .container
      navbar
      router-view
    footersection
</template>



<script>
import auth from './auth'
import navbar from './components/Navbar'
import footersection from './components/Footer'

export default {
  data () {
    return {
      user: auth.user
    }
  },
  methods: {
    logout () {
      auth.logout()
    }
  },
  components: {
    navbar,
    footersection
  }
}
</script>

<style lang='scss'>

@import './assets/css/animate.css';
@import url(https://fonts.googleapis.com/css?family=Open+Sans);
@import url(https://fonts.googleapis.com/css?family=Inconsolata);
@import url(https://fonts.googleapis.com/css?family=Raleway); 

#app {
  font-family: 'Raleway', 'Source Sans Pro',  Helvetica, Arial, sans-serif;
  font-size:16px;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
  margin-top: 60px;
}
.el-select-dropdown, .el-input__inner {
  font-family: 'Raleway', 'Source Sans Pro',  Helvetica, Arial, sans-serif;
}
html {
  position: relative;
  min-height: 100%;
}

body {
  /* Margin bottom by footer height */
  margin-bottom: 60px;
}

.container {
  width:850px;
  max-width:95%;
  margin: 0px auto;
}

.el-button {
  font-size: 18px;
}

.el-button.center {
  display: block;
  margin: 2em auto;
}

.el-alert {
  background-color: white;
  border-radius: 10px;
  border: 2px solid red;
  color: red;
}

h1, h2 {
  text-align: center;
  margin-bottom:1em;
  font-weight: normal
}

h1 { font-size: 3em; }
h2 { font-size: 2em; }

img.icon {
  display: block;
  margin: 0 auto;
  max-width: 100px;
}

.center {
  text-align: center;
}


.router-link-active {
    color: "black";
}
</style>
