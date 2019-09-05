#! /usr/bin/env python3
# coding: UTF-8

""" views of the application """

# import library
from flask import Flask, render_template


# import of the configuration variables
APP = Flask(__name__)
APP.config.from_object('config')


@APP.route('/')
def index():
    """ display the html web page """
    return render_template('index.html')
