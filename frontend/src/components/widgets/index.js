export default function install (Vue) {
  Vue.component('backend-querier', require('./BackendQuerier').default)
  Vue.component('progress-bars', require('./ProgressBars').default)
  Vue.component('learn-more', require('./LearnMore').default)
  Vue.component('download-button', require('./DownloadButton').default)
  Vue.component('helper', require('./Helper').default)
  Vue.component('powered-by', require('./PoweredBy').default)
  Vue.component('files-uploader', require('./FilesUploader').default)
  Vue.component('examples-dialog', require('./ExamplesDialog').default)
  Vue.component('web-links', require('./WebLinks').default)
}
