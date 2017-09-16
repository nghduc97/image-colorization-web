export default {
  namespaced: true,
  state: {
    currentPage: null
  },
  getters: {
    pageName: state => state.currentPage
  },
  mutations: {
    changePage (state, page) {
      state.currentPage = page
    }
  }
}
