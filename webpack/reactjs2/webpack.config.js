const path = require("path");

module.exports = {
  entry: path.resolve("./src/index.js"),
  output: {
    path: path.resolve("./build"),
    filename: "main.js"
  },
  module: {
    rules: [
      { test: /\.jsx?$/, exclude: /node_modules/, use: ["babel-loader"] },
      {
        test: /\.scss/,
        exclude: /node_modules/,
        use: ["style-loader", "css-loader", "less-loader"]
      }
    ]
  },
  resolve: {
    extensions: ["js", "jsx"]
  },
  devServer: {
    contentBase: path.resolve("./build"),
    port: 9000,
    progress: true
  }
};
