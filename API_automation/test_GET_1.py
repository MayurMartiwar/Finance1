import json
import pytest
import jsonpath
import requests


def test_get_1():
    url = "https://staginternalapi.1mg.com/finance_service/v1/tasks/81df7470-b891-4518-b36d-8a24c236b033/54364034653"
    response = requests.get(url)
    json_response = json.loads(response.text)
    id = jsonpath.jsonpath(json_response, 'data.id')
    assert id ==400
