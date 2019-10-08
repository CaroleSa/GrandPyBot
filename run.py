#! /usr/bin/env python3
# coding: UTF-8

""" run program """

# import
from webapp.views import APP

# execute only if run as a script
if __name__ == "__main__":
    APP.run(debug=True)
