#! /usr/bin/env python3
# coding: UTF-8

""" views of the application """

# import library
from flask import Flask, render_template, request
import program.parser as p


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
    if "search" in request.form:
        question = request.form["search"]

        # parser la question et récupérer le lieu recherché
        new_parser = p.Parser()
        place = new_parser.get_place_searched(question)

        return jsonify(dict(results=place))


"""if __name__ == "__main__":
    APP.run()"""
