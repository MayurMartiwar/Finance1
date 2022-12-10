import requests
import json
import jsonpath
def test_GET():
    # API URL
    url = "https://reqres.in/api/users?page=2"

    #Send get Request
    global response
    response = requests.get(url)

    #Display Response Content
    print(response.content)
    print(response.headers)

def test_statuscode():
    #Validate status code
    print(response.status_code)
    assert response.status_code==400

def test_headers():
    #Fetch Response Header
    print(response.headers)

def test_cookie():
    #Fetch cookies
    print(response.cookies)

def test_encoding():
    #Fetch Encoding
    print(response.encoding)

def test_elapseTime():
    #Fetch Elapsed
    print(response.elapsed)