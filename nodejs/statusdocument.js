var axios = require("axios").default;

var options = {
  method: 'POST',
  url: 'https://mex10.com/sign/api/',
  headers: {'Content-Type': 'application/x-www-form-urlencoded'},
  data: {
    token: '44c233a31907139a06c7124c9b0d4c648',
    type: 'STATUS',
    code: 'c9b8253d-dc66-4fe8-9b1b-3e5002e71394'
  }
};

axios.request(options).then(function (response) {
  console.log(response.data);
}).catch(function (error) {
  console.error(error);
});
