import Axios from 'axios'

export const getImageUrls = (postId) => {
  const common = Axios.defaults.baseURL + '/image'
  return {
    originalImage: common + `/original/${postId}`,
    paintedImage: common + `/painted/${postId}`
  }
}
