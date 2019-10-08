#! /usr/bin/env python3
# coding: UTF-8


""" views of the application """



# imports
import random
from flask import Flask, render_template, request, jsonify
from webapp.classes.parser import Parser
from webapp.classes.call_api import CallApi
from config import GOOGLE_KEY

APP = Flask(__name__)



@APP.route('/')
def index():
    """ Display the web page """
    return render_template('index.html', key=GOOGLE_KEY)

@APP.route("/process", methods=["POST"])
def process():
    """ Builds and returns the answer of Grandpy bot """
    # get the user's question
    question = request.form['question']


    # if user's question contains less than one character
    if len(question) <= 1:
        # GrandPy Bot's answer
        text_error_list = ["Tu n'es pas très bavard !",
                           "Dis-moi... où souhaites-tu aller ?",
                           "Euh... oui ?", "Allo ! Il y a quelqu'un ?"]
        random_index = random.randint(0, 3)
        text_error = text_error_list[random_index]
        return jsonify({'error': text_error})


    # if user's question contains more than one character
    # get the place searched
    new_parser = Parser()
    place = new_parser.get_place_searched(question)


    # if the question does not contain the place
    if not place:
        # GrandPy Bot's answer
        text_error_list = ["Je n'ai pas vraiment compris où tu voulais aller ...",
                           "Où veux-tu en venir ?",
                           "Désolé ! Je ne suis pas programmé pour discuter, "
                           "même si tu sembles très sympathique !"]
        random_index = random.randint(0, 2)
        text_error = text_error_list[random_index]
        return jsonify({'error': text_error})


    # if the question contains the place
    new_call_api = CallApi()
    try:
        data_google = new_call_api.call_api_google_maps(place)
    except:
        # GrandPy Bot's answer
        return jsonify({'error': "Il semble que la connexion "
                                 "soit interrompue..."})


    # if Google A.P.I. has no information about the place searched
    if data_google is False:
        text_error = "Je ne trouve rien dans mon carnet d'adresses !"
        return jsonify({'error': text_error})


    # if Google A.P.I. has information about the place searched
    # get data
    name = data_google.get("name")
    address = data_google.get("address")
    latitude = data_google.get("latitude")
    longitude = data_google.get("longitude")
    try:
        data_wiki = new_call_api.call_api_wikipedia(name)
    except:
        # GrandPy Bot's answer
        return jsonify({'error': "Il semble que la connexion "
                                 "soit interrompue..."})
    # GrandPy Bot's answer
    text_address = "Voici l'adresse que j'ai trouvée dans mon carnet pour {} :" \
                   "<br>{}.".format(name, address)
    text_map = "Tiens ! Jette un coup d'oeil sur ma carte !<br>" \
               "Tu peux cliquer sur le carré blanc pour l'agrandir ..."


    # if Wikipédia A.P.I. has no information about the place searched
    if data_wiki is False:
        # GrandPy Bot's answer
        text_history_list = ["Je n'y suis jamais allé... C'est quoi ? Une pizzeria ?",
                             "Je n'en sais pas plus sur cet endroit.",
                             "Pour moi, cet endroit fait encore parti "
                             "des lieux à visiter !",
                             "Il parait qu'il y a de jolies choses à voir la bas !"]
        random_index = random.randint(0, 3)
        text_history = text_history_list[random_index]


    # if Wikipédia A.P.I. has information about the place searched
    else:
        # get data
        history = data_wiki.get("history")
        url = data_wiki.get("url")
        # GrandPy Bot's answer
        text_list = ["J'y ai retrouvé un ami pas plus tard qu'hier ...",
                     "Je m'y promène régulièrement ...",
                     "J'y vais souvent pour faire du Yoga !"]
        random_index = random.randint(0, 2)
        text = text_list[random_index]
        text_history = "Sais-tu que je connais très bien cet endroit ?" \
                       "<br>{}<br>{} Oups ! Désolé, je suis un peu bavard... " \
                       "regardes <a href={} target='_blank'>ICI</a> " \
                       "si tu veux en savoir plus.".format(text, history, url)

    return jsonify({'latitude': latitude, 'longitude': longitude,
                    'address': text_address, 'history': text_history,
                    'map': text_map})
