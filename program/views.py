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
        return jsonify({'error': "Tu n'as rien demandé..."})

    # parser la question et récupérer les informations du lieu recherché
    new_parser = p.Parser()
    place_searched = new_parser.get_place_searched(question)
    if not place_searched:
        return jsonify({'error' : "Je n'ai pas compris ta question."})

    # get place searched informations
    new_call_api_maps = ca.CallApiMaps()
    new_call_api_wiki = ca.CallApiWikipedia()
    data = new_call_api_maps.get_place_data(place_searched)
    if not data:
        return jsonify({'error': "Je connais cet endroit, mais " +
                                 "je ne sais plus où c'est."})

    address = data['candidates'][0]["formatted_address"]
    latitude = data['candidates'][0]["geometry"]["location"]['lat']
    longitude = data['candidates'][0]["geometry"]["location"]['lng']
    history = new_call_api_wiki.get_place_history(place_searched)
    link =

    return jsonify({'latitude': latitude, 'longitude': longitude,
                    'address': address, 'history': history,
                    'link': link})

"""if __name__ == "__main__":
    APP.run()"""