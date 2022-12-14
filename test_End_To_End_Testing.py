import requests
import json
import jsonpath
import pytest

def test_Post_method():
    url = "https://staginternalapi.1mg.com/finance_service/v1/tasks"
    print("------------------1")
    with open('post1.json', 'r') as file:
        print("------------------2")
        data = json.dumps(json.load(file))
        print("------------------3")

    response = requests.post(url, data)
    print(response)
    print("------------------3")