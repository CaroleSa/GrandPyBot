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

    def get_place_data(self, place):
        """ Loading data of the A.P.I. Google Maps and convert to json """

        # request and getting place data
        url = "https://maps.googleapis.com/maps/api/place/findplacefromtext/json?"
        params = {
            'input': place,
            'inputtype': 'textquery',
            'fields': 'name,formatted_address,geometry',
            'key': self.api_google_maps_key
        }
        request = requests.get(url=url, params=params)

        # convert data to json format
        data = request.json()

        return data


class CallApiWikipedia:
    """ Call A.P.I. Wikipedia """

    def __init__(self):
        # select language and format
        self.wiki = wikipediaapi.Wikipedia(
            language='fr',
            extract_format=wikipediaapi.ExtractFormat.WIKI
        )

    def get_place_history(self, place):
        """ Loading data of the A.P.I. Wikipedia """
        # select wikipedia page
        p_wiki = self.wiki.page(place)
        print(p_wiki.summary)

        # display the text if existing wikipedia page : place history
        if len(p_wiki.summary) > 10:
            # get the page link
            url = p_wiki.fullurl

            # get the description of the place
            place_history = p_wiki.summary
            # get index of the point
            index = place_history.find(".", 200)
            # reduction of the description, add comment and link
            place_history = p_wiki.summary[:index + 1]

            return place_history, url

        # display the text if not existing wikipedia page
        else:
            no_result = ""
            return no_result, no_result

new = CallApiWikipedia()
new.get_place_history("vic la gardiole")