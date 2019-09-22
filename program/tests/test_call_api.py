#! /usr/bin/env python3
# coding: UTF-8



from io import BytesIO
import json
import requests


from program.classes import call_api as ca


class MockResponse:
    '''Mock for requests.get response call'''
    def __init__(self, result, ok=True):
        self.ok = ok
        self.result = result

    def json(self):
        return self.result

class TestGoogleApi:
    '''Testing the google api methods calls'''

    def setup_method(self):
        self.place = "lyon"

    def test_search_ok(self, monkeypatch):
        def mockreturn(url, params):
            return MockResponse({
            'candidates': [{'formatted_address': 'Lyon, France',
                            'geometry': {'location': {'lat': 45.764043, 'lng': 4.835659},
                                         'viewport': {'northeast': {'lat': 45.808425, 'lng': 4.898393},
                                                      'southwest': {'lat': 45.707486, 'lng': 4.7718489}}}}], 'status': 'OK'})
        monkeypatch.setattr(requests, "get", mockreturn)
        new_callapimaps = ca.CallApiMaps()
        assert new_callapimaps.get_place_data(self.place) is not None


