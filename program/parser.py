"""from urllib.request import urlopen
import bs4 as BeautifulSoup

html = urlopen('http://127.0.0.1/').read()
soup = BeautifulSoup.BeautifulSoup(html, features="html.parser")
result = soup.find_all('textarea')[0].get_text()
print(soup)
print(result)

html = open("index.html")
masoupe = BeautifulSoup.BeautifulSoup(html, features="html.parser")"""



class Parser:

    def __init__(self):
        self.user_question = "a Salut toi ! peux-tu me dire quel endroit  a se trouve la part dieu à lyon ?"


    def place_search(self):
        # remove all capital letters
        self.user_question = self.user_question.lower()

        # deleting symbols of the user question
        symbols_list = ["-", "'", "_", ".", ",", ";", ":"]
        for elt in symbols_list:
            self.user_question = self.user_question.replace(elt, " ")

        # transforming the user's question into a list
        list_user_question = self.user_question.split()

        # deleting the verbs and subjects of the user question
        subject_list = ["je", "tu", "il", "nous", "vous", "ils"]
        for elt in subject_list:
            while elt in list_user_question:
                verbs_index = list_user_question.index(elt) + 1
                subject_index = list_user_question.index(elt)
                del list_user_question[verbs_index]
                del list_user_question[subject_index]

        # deleting the common words of the user question
        with open("common_words.txt", "r") as f:
            file = f.readlines()
            for word in file:
                word = word.replace("\n", "")
                while word in list_user_question:
                    list_user_question.remove(word)

        # deleting the elements that contain one letter of the user question
        for elt in list_user_question:
            if len(elt) <= 1:
                list_user_question.remove(elt)

        print("resultat", list_user_question)

new_parser = Parser()
new_parser.place_search()


"""f = open('common_words.txt', 'w')
        for elt in common_words:
            f.write("\n {}".format(elt).replace(" ",""))
        f.close()"""
