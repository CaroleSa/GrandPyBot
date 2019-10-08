#! /usr/bin/env python3
# coding: UTF-8

""" Class TestApi """



# imports
from unittest.mock import patch
from unittest import TestCase
from webapp.classes.call_api import CallApi



class TestApi(TestCase):
    """ Call api tests """


    def setUp(self):
        self.new_call_api = CallApi()


    @patch('webapp.classes.call_api.requests.get')
    def test_no_return_google_api(self, mock_api):
        """ Test the False return of the call_api_google_maps function """
        result_json = {'candidates': [], 'status': 'ZERO_RESULTS'}
        mock_api.return_value.json.return_value = result_json

        result = False

        self.assertEqual(self.new_call_api.call_api_google_maps('hhhhh'), result)


    @patch('webapp.classes.call_api.requests.get')
    def test_return_google_api(self, mock_api):
        """ Test the return of the call_api_google_maps function """
        result_json = {'candidates': [{'formatted_address': 'Lyon, France',
                                       'geometry': {'location': {'lat': 45.764043, 'lng': 4.835659},
                                                    'viewport': {'northeast': {'lat': 45.808425,
                                                                               'lng': 4.898393},
                                                                 'southwest': {'lat': 45.707486,
                                                                               'lng': 4.7718489}}},
                                       'name': 'Lyon'}], 'status': 'OK'}
        mock_api.return_value.json.return_value = result_json

        result = {'name': result_json['candidates'][0]["name"],
                  'address': result_json['candidates'][0]["formatted_address"],
                  'latitude': result_json['candidates'][0]["geometry"]["location"]['lat'],
                  'longitude': result_json['candidates'][0]["geometry"]["location"]['lng']}

        self.assertEqual(self.new_call_api.call_api_google_maps('lyon'), result)


    @patch('webapp.classes.call_api.wikipediaapi.Wikipedia.page.fullurl')
    @patch('webapp.classes.call_api.wikipediaapi.Wikipedia.page.summary')
    @patch("webapp.classes.call_api.wikipediaapi.Wikipedia.page")
    def test_return_wikipedia_api(self, mock_url, mock_summary, mock_page):
        """ Test the return of the call_api_wikipedia function """
        if mock_page is True:
            url = mock_url.return_value = "https://fr.wikipedia.org/wiki/OpenClassrooms"
            summary = mock_summary.return_value = "OpenClassrooms est une école en ligne " \
                                                  "qui propose à ses membres des cours " \
                                                  "certifiants et des parcours débouchant sur " \
                                                  "un métier d'avenir, réalisés en interne, " \
                                                  "par des écoles, des universités, " \
                                                  "ou encore par des entreprises partenaires " \
                                                  "comme Microsoft ou IBM."
            index = summary.find(".", 200)
            place_history = summary[:index + 1]

            result = {'history': place_history, 'url': url}

            self.assertEqual(self.new_call_api.call_api_wikipedia('OpenClassrooms'), result)


    @patch("webapp.classes.call_api.wikipediaapi.Wikipedia.page")
    def test_no_return_wikipedia_api(self, mock_page):
        """ Test the False return of the call_api_wikipedia function """
        if mock_page is False:
            result = False
            self.assertEqual(self.new_call_api.call_api_wikipedia('openclassrooms'), result)
