<template>
  <section>
    <hero
      title="Dashboard"
      subtitle="Check out latest and most popular posts on the forum."
      >
    </hero>

    <section class="section">
      <h1 class="title" style="display: inline-block">Popular Images</h1>
      <b-tag class="is-accent is-medium">
        <p>Click on the image to see <strong>Magic</strong></p>
      </b-tag>
      <hr>
      <post-list :post-type="1" sort-by="clap" :limit="4">
      </post-list>
    </section>

    <section class="section">
      <h1 class="title" style="display: inline-block">Latest Images</h1>
      <b-tag class="is-accent is-medium">
        <p>Click on the image to see <strong>Magic</strong></p>
      </b-tag>
      <hr>
      <post-list :post-type="1" sort-by="time" :limit="4">
      </post-list>
    </section>

    <section class="section">
      <h1 class="title">Popular Discusses</h1>
      <hr>
      <post-list :post-type="2" sort-by="clap">
      </post-list>
    </section>

    <section class="section">
      <h1 class="title">Latest Discusses</h1>
      <hr>
      <post-list :post-type="2" sort-by="time"></post-list>
    </section>

    <button class="fab button is-accent" @click="showAddPost = true">
      <b-icon icon="plus"></b-icon>
    </button>

    <b-modal :active.sync="showAddPost">
      <div class="modal-card has-text-centered">
        <b-tabs>
          <b-tab-item label="Image">
            <section class="modal-card-body">
              <b-field>
                <b-input v-model="newPostTitle" placeholder="Title" required></b-input>
              </b-field>
              <b-field>
                <b-upload v-model="newPostFiles" drag-drop accept=".jpg,.jpeg,.png" @input="onImageSelect">
                  <section class="section">
                    <div class="content has-text-centered">
                      <p>
                        <b-icon icon="upload" size="is-large"></b-icon>
                      </p>
                      <p>Drop your image here or click to upload</p>
                    </div>
                  </section>
                </b-upload>
              </b-field>
            </section>
            <footer class="modal-card-foot">
              <button class="button is-primary is-fullwidth" @click="postImage">Post</button>
            </footer>
          </b-tab-item>

          <b-tab-item label="Discuss">
            <section class="modal-card-body">
              <b-field>
                <b-input v-model="newPostTitle" placeholder="Title" required></b-input>
              </b-field>
              <b-field>
                <b-input v-model="newPostContent" type="textarea" placeholder="Content" required></b-input>
              </b-field>
            </section>
            <footer class="modal-card-foot">
              <button class="button is-primary is-fullwidth" @click="postDiscuss">Post</button>
            </footer>
          </b-tab-item>
        </b-tabs>
      </div>
    </b-modal>
  </section>
</template>

<script>
import Axios from 'axios'
import { mapState } from 'vuex'
import PostList from './PostList'
import Hero from './Hero'

export default {
  data () {
    return {
      showAddPost: false,
      newPostTitle: '',
      newPostContent: '',
      newPostFiles: [],
      newPostFileUrl: ''
    }
  },
  computed: {
    ...mapState('auth', ['userInfo'])
  },
  methods: {
    async sendPost (data) {
      try {
        await Axios.post('/post', data)
        this.showAddPost = false
      } catch (err) {
        this.errorMsg('Upload is either invalid or couldn\'t reach server.')
      }
    },
    postDiscuss () {
      this.sendPost({
        'type': 2,
        'title': this.newPostTitle,
        'content': this.newPostContent
      })
    },
    onImageSelect () {
      const file = this.newPostFiles[0]
      const reader = new FileReader()
      reader.readAsDataURL(file)
      reader.onload = () => {
        this.newPostFileUrl = reader.result
      }
    },
    postImage () {
      this.sendPost({
        'type': 1,
        'title': this.newPostTitle,
        'file_b64': this.newPostFileUrl
      })
    }
  },
  components: {
    'post-list': PostList,
    'hero': Hero
  }
}
</script>

<style scoped lang="scss">
.section {
  padding-bottom: 0;
}

.fab {
  position: fixed;
  bottom: 1rem;
  right: 1rem;
  border-radius: 50%;
  width: 3rem;
  height: 3rem;
}

.b-tabs {
  background-color: white;
  border-radius: 4px;

  /deep/ .tabs {
    line-height: 2.5;
  }
}

@import "../color";
.tag strong {
  color: $white;
}
</style>
