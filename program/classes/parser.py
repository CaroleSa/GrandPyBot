#! /usr/bin/env python3
# coding: UTF-8


class Parser:
    """ Parse the question of the user """

    def get_place_searched(self, user_question):
        # remove all capital letters
        user_question = user_question.lower()

        # deleting the symbols of the user question
        with open("program/classes/symbols.txt", "r") as f:
            file = f.readlines()
            print(file)
            for symbol in file:
                symbol = symbol.replace("\n", "")
                user_question = user_question.replace(symbol, " ")

        # transforming the user's question into a list
        list_user_question = user_question.split()

        # deleting the common words of the user question
        with open("program/classes/common_words.txt", "r") as f:
            file = f.readlines()
            for word in file:
                word = word.replace("\n", "")
                while word in list_user_question:
                    list_user_question.remove(word)

        place = " ".join(list_user_question)

        return place

"""new_parser = Parser()
new_parser.get_place_searched("j'ai ramassé des fleurs")"""
