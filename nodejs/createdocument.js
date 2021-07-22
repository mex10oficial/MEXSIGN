var axios = require("axios").default;

var options = {
  method: 'POST',
  url: 'https://mex10.com/sign/api/',
  headers: {'Content-Type': 'application/x-www-form-urlencoded'},
  data: {
    token: 'c7124c9b0d4c648',
    type: 'SIGN',
    namepdf: 'Nome do documento',
    obs: 'observação do documento',
    refer: 'observação do documento',
    users: '{\n  "users":[  \n  {"name":"Nome","phone":"11989898989","email":"email@email.com"},\n  {"name":"NomeSilva","phone":"11989778989","email":"silva@email.com"}  \n  ]\n}',
    pdf: ''
  }
};

axios.request(options).then(function (response) {
  console.log(response.data);
}).catch(function (error) {
  console.error(error);
});
