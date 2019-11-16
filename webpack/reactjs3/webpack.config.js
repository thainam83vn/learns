const path = require("path");

module.exports = {
  entry: path.resolve("./src/index.js"),
  output: {
    path: path.resolve("./build"),
    filename: "main.js"
  },
  devServer: {
    contentBase: path.resolve("./build"),
    port: 9000,
    progress: true
  },
  module: {
    rules: [
      { test: /\.jsx?$/, exclude: /node_modules/, use: ["babel-loader"] },
      {
        test: /\.scss/,
        use: ["style-loader", "css-loader", "less-loader"]
      }
    ]
  }
};
