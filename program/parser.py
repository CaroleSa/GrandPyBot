#! /usr/bin/env python3
# coding: UTF-8


class Parser:
    """ Parse the question of the user """

    def get_place_searched(self, user_question):
        # remove all capital letters
        user_question = user_question.lower()

        # deleting the symbols of the user question
        with open("symbols.txt", "r") as f:
            file = f.readlines()
            for symbol in file:
                symbol = symbol.replace("\n", "")
                user_question = user_question.replace(symbol, " ")

        # transforming the user's question into a list
        list_user_question = user_question.split()

        # deleting the common words of the user question
        with open("common_words.txt", "r") as f:
            file = f.readlines()
            for word in file:
                word = word.replace("\n", "")
                while word in list_user_question:
                    list_user_question.remove(word)

        print(list_user_question)
        return list_user_question

#new_parser = Parser()
#new_parser.get_place_searched("merci de m'indiquer l'endroit ou se trouve la ville de caluire")
