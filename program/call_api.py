#! /usr/bin/env python3
# coding: UTF-8

""" Class CallApiMaps and CallApiWikipedia """



# import
import requests
import wikipediaapi



class CallApiMaps:
    """ Call A.P.I. Google maps """
    def __init__(self):
        self.place = ""
        self.api_google_maps_key = ""

    def load_data(self):
        """ Loading data of the A.P.I. Google Maps and convert to json """
        payload = {'center': self.place, 'zoom': '13', 'size': '600x300',
                   'maptype': 'roadmap', 'markers': 'color:blue%7Clabel:S%7C40.702147,-74.015794',
                   'key': self.api_google_maps_key}
        request = requests.get("https://maps.googleapis.com/maps/api/staticmap?", params=payload)
        data = request.json()
        return data


class CallApiWikipedia:
    """ Call A.P.I. Wikipedia """
    def __init__(self):
        self.new_CallApiMaps = CallApiMaps()
        self.place = self.new_CallApiMaps.place

    def load_data(self):
        """ Loading data of the A.P.I. Wikipedia and convert to json """

        # select language and format
        wiki = wikipediaapi.Wikipedia(
            language='fr',
            extract_format=wikipediaapi.ExtractFormat.WIKI
        )

        # select wikipedia page
        p_wiki = wiki.page("lyon")

        # display the text if existing wikipedia page
        if p_wiki.exists() is True:
            print(p_wiki.summary)

        # display the text if not existing wikipedia page
        else:
            print("la page n'existe pas")

new_call=CallApiWikipedia()
new_call.load_data()
