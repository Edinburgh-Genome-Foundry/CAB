<template lang='pug'>
div
  input(type='text', size='25', value='', v-model='honeypot', :style="{display: 'none'}")
  el-button.center(v-if='submitButtonText.length > 0' @click='submit()', :disabled='status.polling.inProgress') {{submitButtonText }}
  .polling(v-if='status.polling.inProgress && showProgress')

    .polling-message {{status.polling.data.message}}
    el-steps(:space='100', :active='progressStage')
      el-step(icon='upload')
      el-step(icon='setting')
      el-step.last-step(icon='message')
    img.spinner(src='../../assets/images/cab-spinner.svg')
</template>

<script>
import downloadbutton from './DownloadButton'
import spinner from 'vue-spinner/src/PulseLoader'

export default {
  name: 'backend-querier',
  props: {
    submitButtonText: {default: ''},
    value: {default: () => ({})},
    backendUrl: {default: ''},
    backendIP: {default: 'auto'},
    form: {default: () => ({})},
    validateForm: {default: () => () => ([])},
    showProgress: {default: true},
    submitTrigger: {default: false}
  },
  data: function () {
    console.log(this.backendIP === 'auto' ? this.computeBackendIP() : this.backendIP)
    return {
      honeypot: '',
      backendRoot: this.backendIP === 'auto' ? this.computeBackendIP() : this.backendIP,
      status: {
        polling: {
          inProgress: false,
          status: 'queued',
          data: {message: ''}
        },
        result: {},
        requestError: ''
      }
    }
  },
  components: {
    downloadbutton,
    spinner
  },
  watch: {
    value: {
      handler: function (val) {
        this.status = val
      },
      deep: true
    },
    status: {
      handler: function (val) {
        console.log(val)
        this.$emit('input', val)
      },
      deep: true
    },
    submitTrigger: function (value) {
      if (value) {
        this.submit()
      }
    }
  },
  computed: {
    fulldata: function () {
      return {
        data: this.form,
        honeypot: this.honeypot
      }
    },
    progressStage: function () {
      return ['sending', 'queued', 'started', 'finished'].indexOf(this.status.polling.status)
    }
  },
  methods: {
    submit: function () {
      var errors = this.validateForm()
      if (errors.length) {
        this.status.requestError = 'Invalid form: ' + errors.join('   ')
        return false
      }
      this.status.polling.inProgress = true
      this.status.polling.data = {message: 'Contacting the server...'}

      this.$http.post(
        this.backendRoot + this.backendUrl,
        this.form
      ).then(function (response) {
        // SUCCESS
        console.log('job-start response', response)
        this.startPolling(response.body.job_id)
      }, function (response) {
        // FAILURE OF THE JOB STARTING
        console.log('job-start error response', response)
        this.status.requestError = 'Failed with status ' + response.status
        this.status.polling.inProgress = false
        if (response.status === 400) {
          this.status.requestError = 'Bad Request: ' + window.JSON.stringify(response.body)
        }
      })
    },
    startPolling: function (jobId) {
      var self = this
      this.status.polling.inProgress = true
      var jobPoller = setInterval(function () {
        this.$http.post(
          this.backendRoot + 'poll',
          {job_id: jobId}
        ).then(function (pollResponse) {
          // console.log('poll response', pollResponse)
          this.status.requestError = pollResponse.error
          var data = pollResponse.body
          this.status.polling.status = data.status
          if (data.success === false) {
            self.status.requestError = data.error
            self.status.polling.inProgress = false
            clearInterval(jobPoller)
          } else if (data.status === 'queued') {
            self.status.polling.data.message = 'Job pending...'
          } else if (data.status === 'started') {
            self.status.polling.data = data.progress_data
          } else if (data.status === 'finished') {
            self.status.polling.data.message = 'Finished !'
            self.status.result = data.result
            if (data.result.error) {
              self.status.requestError = 'Program error: ' + data.result.error.message
            }
            self.status.polling.inProgress = false
            clearInterval(jobPoller)
          }
          this.status.polling.data.message = data.progress_data.message
        }, function (pollResponse) {
          // FAILURE OF THE POLLING
          this.status.polling.inProgress = false
          this.status.requestError = 'Failed with status ' + pollResponse.status
          clearInterval(jobPoller)
        })
      }.bind(this), 250)
    },
    computeBackendIP: function () {
      var location = window.location.origin
      if (location[location.length - 5] === ':') {
        location = location.slice(0, location.length - 5)
      }
      return location + '/api/'
    }
  }
}
</script>

<style scoped>

.submit-button {
  margin-top: 20px;
  margin-bottom: 60px;
  width: 150px;
}

.el-alert {
  margin: 15px auto 15px;
  width: auto;
  font-size: 14px;
  max-width: 700px;
  padding-right: 40px
}

.polling {
  text-align:center;
  margin-top: 50px
}

.last-step {
  width: 40px !important;
}

.spinner {
  width: 120px;
  margin-top: 2em;
}

</style>
