const path = require('path')

module.exports = {
  outputDir: path.resolve(__dirname, "../" + "main/resources/static"),
  assetsDir: "./",

  devServer: {
    proxy: {
      '/api': {
        target: "http://localhost:8080",
        ws: true,
        changeOrigin: true
      }
    }
  },

  transpileDependencies: [
    'material'
  ]
}
