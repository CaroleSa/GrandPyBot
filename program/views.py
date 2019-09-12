#! /usr/bin/env python3
# coding: UTF-8

""" views of the application """

# import library
from flask import Flask, render_template, request, jsonify
import program.controller as c



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
    question = request.form["test"]
    print(question)

    # parser la question et récupérer les informations du lieu recherché
    new_controller = c.Controller()
    place_info = new_controller.get_place_info(question)

    return jsonify(place_info)

"""if __name__ == "__main__":
    APP.run()"""