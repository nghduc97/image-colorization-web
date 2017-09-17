export const jws = {
  getPayload (token) {
    const firstDot = token.indexOf('.')
    const secondDot = token.indexOf('.', firstDot + 1)
    if (firstDot < 0 || secondDot < 0) throw Error('Invalid JWS')

    return atob(token.slice(firstDot + 1, secondDot))
  }
}
