const config = {
    apiUrl: "http://51.20.3.206/scrape/devops" || process.env.REACT_APP_API_URL,
  };
  console.log("API URL: ", this.apiUrl)
  module.exports = config;