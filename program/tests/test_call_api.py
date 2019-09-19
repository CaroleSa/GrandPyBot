#! /usr/bin/env python3
# coding: UTF-8



from io import BytesIO
import json
import requests


from program.classes import call_api as ca



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
        return {"mock_key": "mock_response"}

    # apply the monkeypatch for requests.get to mock_get
    monkeypatch.setattr(requests, "get", mockreturn)

    # app.get_json, which contains requests.get, uses the monkeypatch
    new_callapimaps = ca.CallApiMaps()
    result = new_callapimaps.get_place_data("toulouse")
    assert result["mock_key"] == "mock_response"




    self.mock = {'product_name_fr': 'product_name',
                 'nutriments': {
                     'nutrition-score-fr': 25},
                 'image_front_url': 'image_url.com',
                 'url': 'url.com'}

    @patch('requests.get')
    def test_imports(self, mock_api):
        """Testing if the method only keep result with every wanted elements"""
        self.response["products"].extend([self.mock, self.mock_no_url,
                                          self.mock_no_img, self.mock_no_score,
                                          self.mock_no_name])
        mock_api.return_value.json.return_value = self.response
        result = ('product_name',
                  25,
                  'image_url.com',
                  'url.com')
        self.assertEqual(self.api.get_products('test'), [result])
