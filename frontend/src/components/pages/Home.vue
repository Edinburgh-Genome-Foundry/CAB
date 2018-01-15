<!-- src/components/Home.vue -->
<template lang="pug">
.home.page
  h1 CAB, the friendly <br /> Computational <br /> App Boilerplate
  web-links(emailSubject='[CAB] Some user feedback',
            tweetMessage="CAB, the friendly Computational App Boilerplate",
            tweetUrl='http://CAB.genomefoundry.org')
  h2 Pick a scenario below.
  .scenario-category(v-for='category in scenarios', :key='category')
    h3 {{category.category}}
    scenariospanel(:scenarios='category.scenarios')
</template>

<script>
import scenariospanel from '../widgets/ScenariosPanel'
import scenarios from '../scenarios/scenarios.js'
export default {
  data: function () {
    return {
      scenarios: scenarios.list
    }
  },
  components: {
    scenariospanel
  }
}
</script>

<style scoped>
h2 {
  margin-bottom: 2em;
  margin-top: 1.5em;
}
p {
  font-size: 18px;
}
</style>
