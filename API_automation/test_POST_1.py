import json
import jsonpath
import requests
import pytest



def test_post_method1():
    url = "https://staginternalapi.1mg.com/finance_service/v1/tasks "
    # f = open('C:/Users/admin/Desktop/API.json', 'r')
    # json_request = json.loads(f.read())
    #
    # response = requests.post(url, json_request)
    # print(response.text)
    with open('post.json') as file:
        data = json.load(file)

    response = requests.post(url, data)

    print(response)
    print(response.status_code)
    assert response.status_code== 200


