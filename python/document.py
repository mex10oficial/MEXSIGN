# importing the requests library
import requests
import base64
import json

# defining the api-endpoint
API_ENDPOINT = "https://mex10.com/sign/api/"

#Global parameters
TOKEN = "44c251c169a06c7124c9b0d4c648"


def send():
    # parameters
    NAME_PDF = 'PDF_EXAMPLE'
    FILE_PDF = '/home/rafael/Downloads/test_grijo.pdf' #Absolute path
    list_users = []

    list_users.append({'name': 'Nome1', 'phone': '1234', 'email': '1234@567.com'})
    list_users.append({'name': 'Nome2', 'phone': '456', 'email': '1234@567.com'})
    list_users.append({'name': 'Nome3', 'phone': '789', 'email': '1234@567.com'})

    users = {'users': list_users}

    #Convert pdf to str base64
    def get_file():
        with open(FILE_PDF, "rb") as pdf_file:
            return base64.b64encode(pdf_file.read())

    # data to be sent to api
    data = {'token': TOKEN,
            'type': 'SIGN',
            'namepdf': NAME_PDF,
            'pdf': get_file(),
            'obs': 'Example',
            'refer': '',
            'users': json.dumps(users)
            }

    # sending post request and saving response as response object
    r = requests.post(url=API_ENDPOINT, data=data)

    # extracting response text
    ret = r.text
    print(ret)

def get_status():
    # data to be sent to api
    data = {'token': TOKEN,
            'type': 'STATUS',
            'code': "bc440bb6-b7d1-4300-83fb-15fc01e7b0ba"
            }

    # sending post request and saving response as response object
    r = requests.post(url=API_ENDPOINT, data=data)

    # extracting response text
    ret = r.text
    print(ret)

#send()
get_status()
