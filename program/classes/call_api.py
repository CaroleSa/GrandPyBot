#! /usr/bin/env python3
# coding: UTF-8

""" Class CallApi """



# imports
import requests
import wikipediaapi
from config import GOOGLE_KEY



class CallApi:
    """ Call A.P.I. Google maps and Wikipédia """


    def __init__(self):
        # select the language and the format
        self.wiki = wikipediaapi.Wikipedia(
            language='fr',
            extract_format=wikipediaapi.ExtractFormat.WIKI
        )

        # get the google key
        self.key = GOOGLE_KEY


    def call_api_google_maps(self, place):
        """ Get the data of the A.P.I. Google Maps and convert to json """

        # request and getting the place data
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

        # if the data exists
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

        # if the data does not exist
        return False


    def call_api_wikipedia(self, place):
        """ Get the data of the A.P.I. Wikipedia """

        # select the Wikipédia page
        p_wiki = self.wiki.page(place)

        # if the page exists
        if p_wiki.exists() is True:
            # get the link
            url = p_wiki.fullurl

            # get the description of the place
            place_history = p_wiki.summary

            # get index of the point
            index = place_history.find(".", 200)
            # reduction of the description
            place_history = p_wiki.summary[:index + 1]

            return {"history": place_history, "url": url}

        # if the page does not exist
        return False
