import requests
import json
import jsonpath
import pytest


def test_post():
    url="https://thetestingworldapi.com/api/studentsDetails"
    with open('postMethod.json') as file:
        data = json.loads(file)

    response = requests.post(url,data)
    print(response.text)
    id = jsonpath.jsonpath(response.json(),"id")
    print(id[0])


def test_get():
    url = "https://thetestingworldapi.com/api/studentsDetails/" + id[0]
    response = requests.get(url)
    print(response.status_code)