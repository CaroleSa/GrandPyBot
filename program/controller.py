#! /usr/bin/env python3
# coding: UTF-8

""" class Controller """


# imports
import program.parser as p
import program.call_api as ca


class Controller:
    """ get place searched informations from user question """

    def __init__(self):
        self.place_searched = ""

    def get_place(self, user_question):
        """ get place searched from user question """
        new_parser = p.Parser()
        self.place_searched = new_parser.get_place_searched(user_question)

    def get_place_info(self):
        """ get and return place searched informations """
        new_call_api_maps = ca.CallApiMaps()
        new_call_api_wiki = ca.CallApiWikipedia()
        coordonates = new_call_api_maps.get_place_coordonates(self.place_searched)
        history = new_call_api_wiki.get_place_history(self.place_searched)

        return coordonates, history
        # résultat obtenu ('Toulouse, France', 43.604652,
        # 1.444209) Toulouse est une commune du Sud-Ouest de la France.
        # Capitale pendant près de cent ans du royaume wisigoth...)
