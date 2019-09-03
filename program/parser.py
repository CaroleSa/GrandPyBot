


class Parser:
    """ Parse the question of the user """

    def __init__(self):
        self.user_question = "Bonjour GrandPyBot ! Peux-tu me dire ou se trouve la bibliothèque de Lyon ?"

        self.place_searched = []

    def get_place_searched(self):
        # remove all capital letters
        self.user_question = self.user_question.lower()

        # deleting the symbols of the user question
        with open("symbols.txt", "r") as f:
            file = f.readlines()
            for symbol in file:
                symbol = symbol.replace("\n", "")
                self.user_question = self.user_question.replace(symbol, " ")

        # transforming the user's question into a list
        list_user_question = self.user_question.split()

        # deleting the common words of the user question
        with open("common_words.txt", "r") as f:
            file = f.readlines()
            for word in file:
                word = word.replace("\n", "")
                while word in list_user_question:
                    list_user_question.remove(word)

        with open("liste_francais.txt", "r") as f:
            file = f.readlines()
            for word in file:
                word = word.replace("\n", "")
                while word in list_user_question:
                    list_user_question.remove(word)

        self.place_searched = list_user_question

        print("resultat", list_user_question)

new_parser = Parser()
new_parser.get_place_searched()
