#! /usr/bin/env python3
# coding: UTF-8

""" Class CallApiMaps and CallApiWikipedia """



# import
import requests
import wikipediaapi



class CallApiMaps:
    """ Call A.P.I. Google maps """

    def __init__(self):
        self.api_google_maps_key = ""

    def get_place_coordonates(self, place):
        """ Loading data of the A.P.I. Google Maps and convert to json """

        # request
        url = "https://maps.googleapis.com/maps/api/place/findplacefromtext/json?"
        params = {
            'input': place,
            'inputtype': 'textquery',
            'fields': 'formatted_address,geometry',
            'key': self.api_google_maps_key
        }
        request = requests.get(url=url, params=params)

        # convert data to json format
        data = request.json()

        # get coordonates of the place
        address = data['candidates'][0]["formatted_address"]
        latitude = data['candidates'][0]["geometry"]["location"]['lat']
        longitude = data['candidates'][0]["geometry"]["location"]['lng']
        # 48.8 pour openclassrooms 2.35

        return address, latitude, longitude


class CallApiWikipedia:
    """ Call A.P.I. Wikipedia """

    def get_place_history(self, place):
        """ Loading data of the A.P.I. Wikipedia and convert to json """

        # select language and format
        wiki = wikipediaapi.Wikipedia(
            language='fr',
            extract_format=wikipediaapi.ExtractFormat.WIKI
        )

        # select wikipedia page
        p_wiki = wiki.page(place)

        # display the text if existing wikipedia page : place history
        if p_wiki.exists() is True:
            place_history = p_wiki.summary

            return place_history

        # display the text if not existing wikipedia page
        else:

            return "la page n'existe pas"
