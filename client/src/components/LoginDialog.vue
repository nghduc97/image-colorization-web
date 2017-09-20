<template>
  <md-dialog md-open-from="#login-button" md-close-to="#login-button" ref="loginDialog">
      <md-dialog-title>Login</md-dialog-title>
      <md-dialog-content>
        <md-input-container md-inline>
          <label>Username</label>
          <md-input v-model="username" ref="usernameInput" @keyup.enter="tryLogin"></md-input>
        </md-input-container>
        <md-input-container md-inline>
          <label>Password</label>
          <md-input type="password" v-model="password" @keyup.enter="tryLogin"></md-input>
        </md-input-container>
        <md-dialog-actions>
          <md-button @click="close">Cancel</md-button>
          <md-button @click="tryLogin" class="md-raised md-primary">Login</md-button>
        </md-dialog-actions>
      </md-dialog-content>
    </md-dialog>
</template>

<script>
export default {
  methods: {
    open () {
      this.$refs.loginDialog.open()
    },
    close () {
      this.$refs.loginDialog.close()
    },
    async tryLogin () {
      await this.$store.dispatch('auth/login', {
        username: this.username,
        password: this.password
      })

      this.username = ''
      this.password = ''
      this.close()
    }
  },
  data () {
    return {
      username: '',
      password: ''
    }
  }
}
</script>

<style>
</style>
