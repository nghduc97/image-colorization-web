<template>
  <section>
    <section class="hero is-primary is-bold">
      <div class="hero-body">
        <div class="container">
          <h1 class="title">
            User Settings
          </h1>
          <h2 class="subtitle">
            Settings for you account
          </h2>
        </div>
      </div>
    </section>
    <section class="section">
      <div class="container">
        <h2 class="title">Account Details</h2>
        <b-field label="Display Name">
          <b-input v-model="accountSettings['display_name']"></b-input>
        </b-field>
        <b-field label="Current Password">
          <b-input type="password" v-model="accountSettings['old_password']"></b-input>
        </b-field>
        <b-field label="New Password">
          <b-input type="password" v-model="accountSettings['new_password']"></b-input>
        </b-field>
        <b-field class="save-button">
          <p class="control">
            <button class="button is-primary" @click="userInfoChange(accountSettings)">
              Save Settings
            </button>
          </p>
        </b-field>
      </div>
    </section>
  </section>
</template>

<script>
import Axios from 'axios'
import { mapState, mapMutations } from 'vuex'

export default {
  data () {
    return {
      accountSettings: {
        'display_name': '',
        'old_password': '',
        'new_password': ''
      }
    }
  },
  computed: {
    ...mapState('auth', ['userInfo'])
  },
  methods: {
    fillSettings () {
      // Account Details
      if (this.userInfo) {
        this.accountSettings['display_name'] = this.userInfo['display_name']
        this.accountSettings['old_password'] = ''
        this.accountSettings['new_password'] = ''
      }
    },
    async userInfoChange (changeInfo) {
      try {
        const data = await Axios.post('/user/info-change', changeInfo)
        this.receiveToken(data)
      } catch (err) {
        this.$toast.open({
          message: 'Network failure or incorrect current password.',
          type: 'is-danger'
        })
      }
    },
    ...mapMutations('auth', ['receiveToken'])
  },
  watch: {
    'userInfo': function (val) {
      this.fillSettings()
    }
  },
  mounted () {
    this.fillSettings()
  }
}
</script>

<style lang="scss">
.save-button {
  margin-top: 2rem;
}
</style>
