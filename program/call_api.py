#! /usr/bin/env python3
# coding: UTF-8

""" Class CallApiMaps and CallApiWikipedia """



# import
import requests
import wikipediaapi
from parser import Parser



class CallApiMaps:
    """ Call A.P.I. Google maps """

    def __init__(self):
        self.api_google_maps_key = ""

        # get place searched by user
        new_parser = Parser()
        self.place = new_parser.place_searched[0]

    def load_data(self):
        """ Loading data of the A.P.I. Google Maps and convert to json """
        URL = "https://maps.googleapis.com/maps/api/staticmap?"
        PARAMS = {
            'center': self.place,
            'zoom': '13',
            'size': '600x300',
            'maptype': 'roadmap',
            'markers': 'color:blue%7Clabel:S%7C40.702147,-74.015794',
            'key': ''
        }
        request = requests.get(url=URL, params=PARAMS)
        print(request)
        data = request.json()
        return data


class CallApiWikipedia:
    """ Call A.P.I. Wikipedia """

    def __init__(self):
        # get place searched by user
        new_parser = p.Parser()
        self.place = new_parser.place_searched[0]

    def get_place_history(self):
        """ Loading data of the A.P.I. Wikipedia and convert to json """

        # select language and format
        wiki = wikipediaapi.Wikipedia(
            language='fr',
            extract_format=wikipediaapi.ExtractFormat.WIKI
        )

        # select wikipedia page
        p_wiki = wiki.page(self.place)

        # display the text if existing wikipedia page
        if p_wiki.exists() is True:
            print(p_wiki.summary)

        # display the text if not existing wikipedia page
        else:
            print("la page n'existe pas")

    def get_place_coordonates(self):
        """ Loading data of the A.P.I. Wikipedia and convert to json """

        URL = "https://en.wikipedia.org/w/api.php"

        PARAMS = {
            "action": "query",
            "format": "json",
            "titles": self.place,
            "prop": "coordinates"
        }

        request = requests.get(url=URL, params=PARAMS)
        data = request.json()
        print(data)
        page = data['query']['pages']

        for k, v in page.items():
            print("Latitute: " + str(v['coordinates'][0]['lat']))
            print("Longitude: " + str(v['coordinates'][0]['lon']))

new_call=CallApiWikipedia()
new_call.get_place_coordonates()
