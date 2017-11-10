<template>
  <section>
    <section class="hero is-primary is-fullheight is-bold has-text-centered">
      <div class="hero-body">
        <div class="container">
          <p class="logo">
            <img src="/static/Logomakr_1zxkZd.png" />
          </p>
          <h2 class="subtitle">
            Welcome to ICW, a forum to try out AI colorization engine.
          </h2>
          <a class="button is-light is-medium show-login-button" @click="showAuthModal = true">
            Login and Join Us
          </a>
        </div>
      </div>
    </section>
    <section>
      <b-modal :active.sync="showAuthModal" ref="authModal">
        <div class="modal-card has-text-centered">
          <b-tabs v-model="activeTab">
            <b-tab-item label="Login">
              <section class="modal-card-body">
                <b-field>
                  <b-input placeholder="Username" v-model="username" required></b-input>
                </b-field>
                <b-field>
                  <b-input type="password" placeholder="Password" v-model="password" required></b-input>
                </b-field>
              </section>
              <footer class="modal-card-foot">
                <button class="button is-primary is-fullwidth" @click="tryLogin">Login</button>
              </footer>
            </b-tab-item>

            <b-tab-item label="Register">
              <section class="modal-card-body">
                <b-field>
                  <b-input placeholder="Display Name" v-model="displayName" required></b-input>
                </b-field>
                <b-field>
                  <b-input placeholder="Username" v-model="username" required></b-input>
                </b-field>
                <b-field>
                  <b-input type="password" password-reveal placeholder="Password" v-model="password" required></b-input>
                </b-field>
              </section>
              <footer class="modal-card-foot">
                <button class="button is-primary is-fullwidth" @click="tryRegister">Register</button>
              </footer>
            </b-tab-item>
          </b-tabs>
        </div>
      </b-modal>
    </section>
  </section>
</template>

<script>
import router from '../router'

export default {
  data () {
    return {
      showAuthModal: false,
      activeTab: 0,
      username: '',
      password: '',
      displayName: ''
    }
  },
  methods: {
    async tryLogin () {
      try {
        await this.$store.dispatch('auth/login', {
          'username': this.username,
          'password': this.password
        })
        this.$refs['authModal'].close()
        router.replace('/dashboard')
      } catch (err) {
        console.error(err)
      }
    },
    async tryRegister () {
      try {
        await this.$store.dispatch('auth/register', {
          'username': this.username,
          'password': this.password,
          'display_name': this.displayName
        })
        this.$refs['authModal'].close()
        router.replace('/dashboard')
      } catch (err) {
        console.error(err)
      }
    }
  }
}
</script>

<style scoped lang="scss">
.logo img {
  height: 5em;
  margin-bottom: 3em;
}

.show-login-button {
  color: #7957d5;
}

.b-tabs {
  background-color: white;
  border-radius: 4px;

  /deep/ .tabs {
    line-height: 2.5;
  }
}
</style>
