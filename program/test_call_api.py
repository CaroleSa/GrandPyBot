#! /usr/bin/env python3
# coding: UTF-8



import urllib.request
from io import BytesIO
import json
import requests


import program.call_api as ca


"""def test_get_place_history():
    new_call_api_wiki = ca.CallApiWikipedia()
    results = new_call_api_wiki.get_place_history("Toulouse")
    assert results[0:24] == "Toulouse est une commune"
    """



# custom class to be the mock return value
# will override the requests.Response returned from requests.get
class MockResponse:

    # mock json() method always returns a specific testing dictionary
    @staticmethod
    def json():
        return {"mock_key": "mock_response"}


def test_get_place_data(monkeypatch):

    # Any arguments may be passed and mock_get() will always return our
    # mocked object, which only has the .json() method.
    def mockreturn(*args, **kwargs):
        return MockResponse()

    # apply the monkeypatch for requests.get to mock_get
    monkeypatch.setattr(requests, "get", mockreturn)

    # app.get_json, which contains requests.get, uses the monkeypatch
    new_callapimaps = ca.CallApiMaps()
    result = new_callapimaps.get_place_data("toulouse")
    assert result["mock_key"] == "mock_response"


