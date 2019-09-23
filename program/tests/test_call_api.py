#! /usr/bin/env python3
# coding: UTF-8



from io import BytesIO
import json
import requests
import wikipediaapi


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
            return MockResponse({'candidates': [{'formatted_address': 'Lyon, France',
                                                 'geometry': {'location': {'lat': 45.764043, 'lng': 4.835659},
                                                              'viewport': {
                                                                  'northeast': {'lat': 45.808425, 'lng': 4.898393},
                                                                  'southwest': {'lat': 45.707486, 'lng': 4.7718489}}},
                                                 'name': 'Lyon'}], 'status': 'OK'})

        monkeypatch.setattr(requests, "get", mockreturn)

        new_ca = ca.CallApi()
        assert new_ca.call_api_google_maps(self.place) == {'name': MockResponse.result['candidates'][0]["name"],
                                                           'address': 'Lyon, France',
                                                           'latitude': 45.764043,
                                                           'longitude': 4.835659}



class MockResponse:
    '''Mock for requests.get response call'''
    def __init__(self, result, ok=True):
        self.ok = ok
        self.result = result

    def json(self):
        return self.result

class TestWikipediaApi:
    '''Testing the google api methods calls'''

    def setup_method(self):
        self.place = "lyon"

    def test_search_ok(self, monkeypatch):
        def mockreturn(language, extract_format):
            return MockResponse({'history': "Lyon (prononcé /ljɔ̃/ ou /liɔ̃/ ) est une commune française située dans le quart sud-est "
                             "de la France au confluent du Rhône et de la Saône. Siège du conseil de la métropole de "
                             "Lyon, elle est le chef-lieu de l'arrondissement de Lyon, de la circonscription "
                             "départementale du Rhône et de la région Auvergne-Rhône-Alpes.",
                  'url': 'https://fr.wikipedia.org/wiki/Lyon'})



        monkeypatch.setattr(wikipediaapi.Wikipedia, "page", mockreturn)


        new_ca = ca.CallApi()
        assert new_ca.call_api_wikipedia(self.place) == {'history': "Lyon (prononcé /ljɔ̃/ ou /liɔ̃/ ) est une commune française située dans le quart sud-est "
                             "de la France au confluent du Rhône et de la Saône. Siège du conseil de la métropole de "
                             "Lyon, elle est le chef-lieu de l'arrondissement de Lyon, de la circonscription "
                             "départementale du Rhône et de la région Auvergne-Rhône-Alpes.",
                  'url': 'https://fr.wikipedia.org/wiki/Lyon'}
