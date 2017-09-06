export default {
  state: {
    currentPage: null
  },
  mutations: {
    changePage (state, page) {
      state.currentPage = page
    }
  }
}
