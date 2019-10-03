#! /usr/bin/env python3
# coding: UTF-8

""" run program """

# import
from program.views import app

# execute only if run as a script
if __name__ == "__main__":
    app.run(debug=True)
