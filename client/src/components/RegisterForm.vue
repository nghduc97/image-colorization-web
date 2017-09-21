<template>
  <md-card style="max-width: 500px; margin: 10px auto;">
    <md-toolbar>
      <h2 class="md-title">Register to Upload Your Own Images</h2>
    </md-toolbar>
    <md-card-area>
      <md-card-content>
        <md-input-container md-inline>
          <label>Display Name</label>
          <md-input v-model="displayName"></md-input>
        </md-input-container>
        <md-input-container md-inline>
          <label>Username</label>
          <md-input v-model="username"></md-input>
        </md-input-container>
        <md-input-container md-inline>
          <label>Password</label>
          <md-input type="password" v-model="password"></md-input>
        </md-input-container>
      </md-card-content>
      <md-card-actions>
        <md-button class="md-raised md-primary" @click="tryRegister">Register</md-button>
      </md-card-actions>
    </md-card-area>
  </md-card>
</template>

<script>
export default {
  data () {
    return {
      username: '',
      password: '',
      displayName: ''
    }
  },
  methods: {
    async tryRegister () {
      await this.$store.dispatch('auth/register', {
        'username': this.username,
        'password': this.password,
        'display_name': this.displayName
      })
    }
  }
}
</script>

<style>

</style>
