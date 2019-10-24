import requests
import json

def normal_requests():
    url = 'http://127.0.0.1:5000/get_user_info'
    method = {'key_word': 'name'}
    headers = {'Content-Type': 'application/json'}
    r = requests.post(url,headers=headers,data=json.dumps(method))
    print(r.content)

def abnormal_requests():
    url = 'http://127.0.0.1:5000/get_user_info'
    method = {'key_word': 'delete'}
    headers = {'Content-Type': 'application/json'}
    r = requests.post(url,headers=headers,data=json.dumps(method))
    print(r.content)

if __name__ == '__main__':
    normal_requests()
    abnormal_requests()