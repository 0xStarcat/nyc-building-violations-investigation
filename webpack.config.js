module.exports = {
  entry: './client/public/app.js',
  output: {
    path: __dirname + '/client-react/public/dist',
    filename: 'bundle.js'
  },
  module: {
    rules: [
      {
        test: /\.scss$/,
        loaders: ['style-loader', 'css-loader', 'sass-loader']
      }
    ]
  }
}
