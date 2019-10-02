#! /usr/bin/env python3
# coding: UTF-8

""" Class CallApi """



# import
import requests
import wikipediaapi
from config import google_key



class CallApi:
    """ Call A.P.I. Google maps """

    def __init__(self):

        # select language and format
        self.wiki = wikipediaapi.Wikipedia(
            language='fr',
            extract_format=wikipediaapi.ExtractFormat.WIKI
        )

        self.key = google_key

    def call_api_google_maps(self, place):
        """ Loading data of the A.P.I. Google Maps and convert to json """

        # request and getting place data
        url = "https://maps.googleapis.com/maps/api/place/findplacefromtext/json?"
        params = {
            'input': place,
            'inputtype': 'textquery',
            'fields': 'name,formatted_address,geometry',
            'key': self.key
        }
        request = requests.get(url=url, params=params)


        # convert data to json format
        data = request.json()

        if data.get("status") == "OK":
            # get datas
            name = data['candidates'][0]["name"]
            address = data['candidates'][0]["formatted_address"]
            latitude = data['candidates'][0]["geometry"]["location"]['lat']
            longitude = data['candidates'][0]["geometry"]["location"]['lng']

            return {
                "name": name,
                "address": address,
                "latitude": latitude,
                "longitude": longitude
            }

        return False



    def call_api_wikipedia(self, place):
        """ Loading data of the A.P.I. Wikipedia """
        # select wikipedia page

        p_wiki = self.wiki.page(place)

        if p_wiki.exists() is True:
           # display the text if existing wikipedia page : place history
            # get the page link
            url = p_wiki.fullurl

            # get the description of the place
            place_history = p_wiki.summary

            # get index of the point
            index = place_history.find(".", 200)
            # reduction of the description, add comment and link
            place_history = p_wiki.summary[:index + 1]

            return {"history": place_history, "url": url}

        return False
