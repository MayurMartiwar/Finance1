import json
import jsonpath
import requests
import pytest


def test_post_method1():
    url = "https://staginternalapi.1mg.com/finance_service/v1/tasks"
    # f = open('C:/Users/admin/Desktop/API.json', 'r')
    # json_request = json.load(f.read())

    # response = requests.post(url, json_request)
    # print(response.text)
    with open('post.json', 'r') as file:

        data = json.dumps(json.load(file))
        global response
    response = requests.post(url, data)
    print(response)
    # test_headers(response)
    # test_cookie(response)
    # test_encoding(response)
    # test_elapseTime(response)

    print(response.json())

    print(response.status_code)
    assert response.status_code == 200


def test_headers():
    # Fetch Response Header
    print(response.headers)

def test_cookie():
    # Fetch cookies
    print(response.cookies)

def test_encoding():
    # Fetch Encoding
    print(response.encoding)

def test_elapseTime():
     # Fetch Elapsed
   print(response.elapsed)

