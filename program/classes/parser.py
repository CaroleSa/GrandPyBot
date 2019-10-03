#! /usr/bin/env python3
# coding: UTF-8

""" Class Parser """


class Parser:
    """ Parse the question of the user """

    @classmethod
    def get_place_searched(cls, user_question):
        """ get place searched in the user's question """

        # remove all capital letters
        user_question = user_question.lower()

        # deleting the symbols of the user question
        with open("program/classes/symbols.txt", "r", encoding="cp1252") as file:
            file = file.readlines()
            for symbol in file:
                symbol = symbol.replace("\n", "")
                user_question = user_question.replace(symbol, " ")

        # transforming the user's question into a list
        list_user_question = user_question.split()

        # deleting the common words of the user question
        with open("program/classes/common_words.txt", "r", encoding="cp1252") as file:
            file = file.readlines()
            for word in file:
                word = word.replace("\n", "")
                while word in list_user_question:
                    list_user_question.remove(word)

        place = " ".join(list_user_question)

        return place
