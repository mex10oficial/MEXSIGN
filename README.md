# MEXSIGN
Api da mex10.com/sign

Endpoint: https://mex10.com/sign/api/

*Todos os parâmetros como FORM DATA


=========== Create document ================

Parameters POST

token: SEUTOKEN (obrigatório)

type: "SIGN"

namepdf: "Nome do documento"(obrigatório)

pdf: PDF convertido em base64(String)(obrigatório)

obs: "observação do documento"(opcional)

refer: "Codigo interno do seu sistema"(opcional)

users: JSON contendo os signatários que irão assinar o documento

{
"users":[
{"name":"Nome","phone":"11989898989","email":"email@email.com"},
{"name":"NomeSilva","phone":"11989778989","email":"silva@email.com"}
]
}

=========== Status document ================

Parameters POST
token: SEUTOKEN (obrigatório)
type: "STATUS"
code: "Código do documento, fornecido na criação"(obrigatório)
