#API URL
import json
import jsonpath
import requests
import pytest

def test_add_data():
    url = "https://reqres.in/api/users "

    # Read Body from JSON FILE
    file = open("C:Users\admin\Desktop\Required Doc. URL ", "r")
    json_request = json.loads(file.read())
    response = requests.post(url , json_request)
    print(response.text)







