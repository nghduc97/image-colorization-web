export default {
  namespaced: true,
  state: {
    currentPage: null
  },
  mutations: {
    changePage (state, page) {
      state.currentPage = page
    }
  }
}
