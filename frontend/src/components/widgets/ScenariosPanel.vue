<template lang="pug">
el-row
	el-col(:xs="24", :sm="12", :md="6", :lg="6" v-for='scenario in scenarios', :key='scenario.default.infos.title')
		el-card.box-card
			img.icon(:src='scenario.default.infos.icon', alt='')
			.caption
				h3 {{scenario.default.infos.title}}
				p.thumbnail-description {{scenario.default.infos.description}}
				router-link(:to='scenario.default.infos.path')
					el-button(type='primary') Go
</template>

<script>
export default {
  props: {
    scenarios: {
      default: () => ([])
    }
  }
}
</script>

<style lang='scss' scoped>
.box-card {
    width: 90%;
    margin: 10px auto;
    text-align: center;
}
img {
    height: 80px;
}
.caption {
    padding: 0;
    h3 {
        height: 50px;
    }
}

.thumbnail-description {
    font-size: 14px;
}
</style>
