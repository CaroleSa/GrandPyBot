#! /usr/bin/env python3
# coding: UTF-8


# imports
from flask import Flask, render_template



# import des variables de configuration
app = Flask(__name__)
app.config.from_object('config')

# affiche le résultat du fichier html sur la page web
@app.route('/')
def index():
    return render_template('index.html')
