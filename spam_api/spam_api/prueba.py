import requests
import json

URL_LOGIN = 'http://localhost:8000/api-token-auth/'

data = {'username':'test','password':'mati1234'}


res_request_login = requests.post(URL_LOGIN, data)
try:
    token = json.loads(res_request_login.content.decode('utf-8'))['token']
    headers = { 'Authorization': f'JWT {token}' }

    res_request_test_if_logged = requests.get('http://localhost:8000/test_if_logged',headers=headers)

    print(res_request_test_if_logged.content)
except:
    print({'error'})

# b'{"token":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6ImZjYXJyaWxsbyIsImV4cCI6MTYwNjE1Mjg1OSwiZW1haWwiOiIifQ.0wG_N1LfvjUT87Jh64v9xxmM4U8JDfFgn3RQrKFoi9A"}'