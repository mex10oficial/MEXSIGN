<?php

$curl = curl_init();

$data = http_build_query(
    [
        "token" => "SEUTOKEN",
        "type" => "SIGN",
        "namepdf" => "Nome do documento",
        "obs" => "observação do documento",
        "refer" => "Codigo interno do seu sistema",
        "users" => '{"users":[{"name":"Nome","phone":"11989898989","email":"email@email.com"},{"name":"NomeSilva","phone":"11989778989","email":"silva@email.com"}]}',
        "pdf" => "DOCUMENTO_EM_BASE64"
    ]
);

curl_setopt_array($curl, [
    CURLOPT_URL => "https://mex10.com/sign/api/",
    CURLOPT_RETURNTRANSFER => true,
    CURLOPT_ENCODING => "",
    CURLOPT_MAXREDIRS => 10,
    CURLOPT_TIMEOUT => 30,
    CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
    CURLOPT_CUSTOMREQUEST => "POST",
    CURLOPT_POSTFIELDS => $data,
    CURLOPT_HTTPHEADER => [
        "Content-Type: application/x-www-form-urlencoded"
    ],
]);

$response = curl_exec($curl);
$err = curl_error($curl);

curl_close($curl);

if ($err) {
    echo "cURL Error #:" . $err;
} else {
    echo $response;
}
