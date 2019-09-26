#! /usr/bin/env python3
# coding: UTF-8


# import de la variable app à partir du fichier __init__
from program.views import app

# point d'entrée du programme
if __name__ == "__main__":
    app.run(debug=True)

