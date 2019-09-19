#! /usr/bin/env python3
# coding: UTF-8

""" views of the application """

# import library
from flask import Flask, render_template, request, jsonify
import program.classes.parser as p
import program.classes.call_api as ca
import random



# import of the configuration variables
APP = Flask(__name__)
APP.config.from_object('config')



@APP.route('/')
def index():
    """ display the html web page """
    return render_template('index.html')

@APP.route("/process", methods=["POST"])
def process():
    # get the user's question and return an error message if no result
    question = request.form['question']
    if not question:
        return jsonify({'error': "Tu n'es pas bavard ..."})

    # get the place searched and return an error message if no result
    new_parser = p.Parser()
    place = new_parser.get_place_searched(question)
    if not place:
        return jsonify({'error': "Je n'ai pas vraiment compris où tu voulais aller ..."})

    else:

        # get the history of the place and create a message
        new_call_api_wiki = ca.CallApiWikipedia()
        history = new_call_api_wiki.get_place_history(place)[0]
        url = new_call_api_wiki.get_place_history(place)[1]
        if len(history) < 10:
            text_history_list = ["Je n'y suis jamais allé... C'est quoi ? Une pizzeria ?", "Je ne connais pas cet endroit",
                                 "Pour moi, cet endroit fait encore parti des lieux à visiter !",
                                 "Il parait qu'il y a de jolies robotes la bas !"]
            random_index = random.randint(0, 3)
            text_history = text_history_list[random_index]
        else:
            text_history = "Sais-tu que je connais très bien cet endroit ?<br>{} <br>Désolé, je suis un peu bavard..." \
                           "regardes ici si tu veux en savoir plus : <a href={} target='_blank'>ICI</a>.".format(history, url)

        # get the address of the place and create a message
        new_call_api_maps = ca.CallApiMaps()
        data = new_call_api_maps.get_place_data(place)
        if not data['candidates']:
            text_address = "Je ne trouve rien dans mon carnet d'adresses !"
            text_map = ""

            # return latitude, longitude and text
            return jsonify({'address': text_address, 'history': text_history, 'map': text_map})

        else:
            address = data['candidates'][0]["formatted_address"]
            text_address = "Voici l'adresse de {} :<br>{}.".format(place, address)
            text_map = "Tiens ! Jette un coup d'oeil sur ma carte !"

            # get the coordinates of the place and create a message
            latitude = data['candidates'][0]["geometry"]["location"]['lat']
            longitude = data['candidates'][0]["geometry"]["location"]['lng']

            # return latitude, longitude and text
            return jsonify({'latitude': latitude, 'longitude': longitude,
                            'address': text_address, 'history': text_history,
                            'map': text_map})

