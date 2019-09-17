#! /usr/bin/env python3
# coding: UTF-8

""" views of the application """

# import library
from flask import Flask, render_template, request, jsonify

import program.parser as p
import program.call_api as ca



# import of the configuration variables
APP = Flask(__name__)
APP.config.from_object('config')


@APP.route('/')
def index():
    """ display the html web page """
    return render_template('index.html')

@APP.route("/process", methods=["POST"])
def process():
    # récupérer la question de l'utilisateur
    question = request.form['question']
    if not question:
        return jsonify({'error': "Tu n'es pas bavard ..."})

    # parser la question et récupérer les informations du lieu recherché
    new_parser = p.Parser()
    place = new_parser.get_place_searched(question)
    if not place:
        return jsonify({'error': "Je n'ai pas vraiment compris où tu voulais aller ..."})

    else:
        # get place searched informations
        new_call_api_maps = ca.CallApiMaps()
        data = new_call_api_maps.get_place_data(place)
        address = data['candidates'][0]["formatted_address"]
        if not address:
            text_address = "Impossible de remettre la main sur mon carnet d'adresses !"
        else:
            text_address = "Voici l'adresse de {} :<br>{}.".format(place, address)

        latitude = data['candidates'][0]["geometry"]["location"]['lat']
        longitude = data['candidates'][0]["geometry"]["location"]['lng']
        if not latitude:
            text_map = "Désolé, j'ai perdu ma carte... je ne vais pas pouvoir te montrer où c'est."
        else:
            text_map = "Tiens ! Jette un coup d'oeil sur cette carte !"

        new_call_api_wiki = ca.CallApiWikipedia()
        history = new_call_api_wiki.get_place_history(place)[0]
        url = new_call_api_wiki.get_place_history(place)[1]
        if len(history) < 10:
            text_history = "Je n'y suis jamais allé... C'est quoi ? Une pizzeria ?"
        else:
            text_history = "Dailleurs ! Sais-tu que je connais très bien cet endroit ?<br>{} <br>Désolé, je suis un peu bavard..." \
                           "regardes ici si tu veux en savoir plus : <a href={} target='_blank'>ICI</a>.".format(history, url)

    return jsonify({'latitude': latitude, 'longitude': longitude,
                    'address': text_address, 'history': text_history,
                    'map': text_map})

if __name__ == "__main__":
    APP.run()
