#! /usr/bin/env python3
# coding: UTF-8

""" class Controller """


# imports
import program.parser as p
import program.call_api as ca


class Controller:
    """ get place searched and its informations from user question """

    def get_place_info(self, user_question):
        """ get and return place searched informations """

        # get place searched from user question
        new_parser = p.Parser()
        place_searched = new_parser.get_place_searched(user_question)

        # get place searched informations
        new_call_api_maps = ca.CallApiMaps()
        new_call_api_wiki = ca.CallApiWikipedia()
        data = new_call_api_maps.get_place_data(place_searched)
        coordinates = new_call_api_maps.get_place_coordinates(data)
        history = new_call_api_wiki.get_place_history(place_searched)

        return coordinates, history
