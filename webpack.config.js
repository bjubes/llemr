const path = require("path");

module.exports = {
  entry: {
    surveys_edit: {
      import: "./osler/assets/surveys/edit/index.js",
      dependOn: "shared",
    },
    surveys_test: {
      import: "./osler/assets/surveys/edit/test.js",
    },
    shared: ["react", "react-dom"],
  },
  output: {
    filename: "[name].bundle.js", // output bundle file name
    chunkFilename: "[id]-[chunkhash].js",
    path: path.resolve(__dirname, "./osler/static/js"),
    publicPath: "osler/static/",
    library: "[name]",
    libraryTarget: "var", // export bar() in index.js and access as [name].bar() in template
  },
  optimization: {
    runtimeChunk: "single",
  },
  devServer: {
    writeToDisk: true, // Write files to disk in dev mode, so Django can serve the assets
  },
  module: {
    rules: [
      {
        test: /\.(js|jsx)$/,
        exclude: /node_modules/,
        loader: "babel-loader",
        options: { presets: ["@babel/preset-env", "@babel/preset-react"] },
      },
    ],
  },
};
