#! /usr/bin/env python3
# coding: UTF-8

""" Class CallApiMaps and CallApiWikipedia """



# import
import requests
import wikipediaapi
import program.parser as p



class CallApiMaps:
    """ Call A.P.I. Google maps """

    def __init__(self):
        self.api_google_maps_key = ""

        # get place searched by user
        new_parser = p.Parser()
        self.place = new_parser.place_searched[0]

        self.address = ""
        self.longitude = ""
        self.latitude = ""

    def get_place_coordonates(self):
        """ Loading data of the A.P.I. Google Maps and convert to json """

        # request
        url = "https://maps.googleapis.com/maps/api/place/findplacefromtext/json?"
        params = {
            'input': self.place,
            'inputtype': 'textquery',
            'fields': 'formatted_address,geometry',
            'key': self.api_google_maps_key
        }
        request = requests.get(url=url, params=params)

        # convert data to json format
        data = request.json()

        # get coordonates of the place
        self.address = data['candidates'][0]["formatted_address"]
        self.latitude = data['candidates'][0]["geometry"]["location"]['lat']
        self.longitude = data['candidates'][0]["geometry"]["location"]['lng']
        # 48.8 pour openclassrooms 2.35


class CallApiWikipedia:
    """ Call A.P.I. Wikipedia """

    def __init__(self):
        # get place searched by user
        new_parser = p.Parser()
        self.place = new_parser.place_searched[0]

        self.place_history = ""

    def get_place_history(self):
        """ Loading data of the A.P.I. Wikipedia and convert to json """

        # select language and format
        wiki = wikipediaapi.Wikipedia(
            language='fr',
            extract_format=wikipediaapi.ExtractFormat.WIKI
        )

        # select wikipedia page
        p_wiki = wiki.page(self.place)

        # display the text if existing wikipedia page : place history
        if p_wiki.exists() is True:
            self.place_history = p_wiki.summary

        # display the text if not existing wikipedia page
        else:
            print("la page n'existe pas")


NEW_CALL = CallApiMaps()
NEW_CALL.get_place_coordonates()
