<template lang='pug'>
  .powered-by
    p Powered by
    .powered-by-logo(v-if='softwareInfos.length == 1')
      a(:href='softwareInfos[0].href')
        img(:src='softwareInfos[0].logoSrc')
        span.software-name {{softwareInfos[0].name}}
    el-row(v-else).powered-by-logos
      el-col.powered-by-logo(:xs="24", :sm="12", :md="12", :lg="12" v-for='item in softwareInfos', :key='item.name')
        a(:href='item.href')
          img(:src='item.logoSrc')
          span.software-name {{item.name}}
</template>


<script>
var allSoftwareInfos = {
  bandwagon: {
    name: 'BandWagon',
    logoSrc: '/static/logos/bandwagon.png',
    href: 'https://github.com/Edinburgh-Genome-Foundry/BandWagon'
  },
  bandwitch: {
    name: 'BandWitch',
    logoSrc: '/static/logos/bandwitch.png',
    href: 'https://github.com/Edinburgh-Genome-Foundry/BandWitch'
  },
  dnacauldron: {
    name: 'DNA Cauldron',
    logoSrc: '/static/logos/dnacauldron.png',
    href: 'https://github.com/Edinburgh-Genome-Foundry/DnaCauldron'
  },
  dnachisel: {
    name: 'DNA Chisel',
    logoSrc: '/static/logos/dnachisel.png',
    href: 'https://github.com/Edinburgh-Genome-Foundry/DnaChisel'
  },
  dnafeaturesviewer: {
    name: 'DNA Features Viewer',
    logoSrc: '/static/logos/dfv.png',
    href: 'https://github.com/Edinburgh-Genome-Foundry/DnaFeaturesViewer'
  },
  goldenhinges: {
    name: 'Golden Hinges',
    logoSrc: '/static/logos/goldenhinges.png',
    href: 'https://github.com/Edinburgh-Genome-Foundry/GoldenHinges'
  },
  geneblocks: {
    name: 'Gene Blocks',
    logoSrc: '/static/logos/geneblocks.png',
    href: 'https://github.com/Edinburgh-Genome-Foundry/Geneblocks'
  },
  caravagene: {
    name: 'Caravagene',
    logoSrc: '/static/logos/caravagene.png',
    href: 'https://github.com/Edinburgh-Genome-Foundry/Caravagene'
  }
}
export default {
  props: {
    softwareNames: {default: () => ([])}
  },
  computed: {
    softwareInfos: function () {
      return this.softwareNames.map(function (name) { return allSoftwareInfos[name] })
    }
  }
}
</script>

<style lang='scss' scoped>
.powered-by {
  margin-top: 10em;
  margin-bottom: 0;
  text-align: center;
  width: 70%;
  margin-left: 15%;
  .powered-by-logo {
    margin-bottom: 30px;
    a {
      text-decoration: none;
      color: #333;
      opacity: 0.7;
      span {
        margin: 0 10px;
        font-size: 19px;
        font-variant: small-caps;
      }

      img {
        display: inline;
        height: 54px;
        margin-bottom: -18px;
      }
    }
  }
}
</style>
