module.exports = {
  entry: './nyc_data_server.js',
  output: {
    path: __dirname + '/build',
    filename: 'nyc_data_server.js'
  },
  module: {
    rules: []
  }
}
