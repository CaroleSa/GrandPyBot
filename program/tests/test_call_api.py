#! /usr/bin/env python3
# coding: UTF-8



from unittest.mock import patch
from unittest import TestCase
from program.classes.call_api import CallApi




class TestApi(TestCase):

    ### TEST ###
    def setUp(self):
        """Setting the Api Classes"""
        self.ca = CallApi()

    @patch('program.classes.call_api.requests.get')
    def test_no_return_google_api(self, mock_api):
        """Testing if the method only keep result with every wanted elements"""

        result_json = {'candidates': [], 'status': 'ZERO_RESULTS'}

        mock_api.return_value.json.return_value = result_json

        result = False

        self.assertEqual(self.ca.call_api_google_maps('hhhhh'), result)


    @patch('program.classes.call_api.requests.get')
    def test_return_google_api(self, mock_api):
        """Testing if the method only keep result with every wanted elements"""

        result_json = {'candidates': [{'formatted_address': 'Lyon, France',
                                       'geometry': {'location': {'lat': 45.764043, 'lng': 4.835659},
                                                    'viewport': {'northeast': {'lat': 45.808425, 'lng': 4.898393},
                                                                 'southwest': {'lat': 45.707486, 'lng': 4.7718489}}},
                                       'name': 'Lyon'}], 'status': 'OK'}

        mock_api.return_value.json.return_value = result_json

        result = {'name': result_json['candidates'][0]["name"],
                  'address': result_json['candidates'][0]["formatted_address"],
                  'latitude': result_json['candidates'][0]["geometry"]["location"]['lat'],
                  'longitude': result_json['candidates'][0]["geometry"]["location"]['lng']}


        self.assertEqual(self.ca.call_api_google_maps('lyon'), result)






    @patch('program.classes.call_api.wikipediaapi.Wikipedia.page.fullurl')
    @patch('program.classes.call_api.wikipediaapi.Wikipedia.page.summary')
    @patch('program.classes.call_api.wikipediaapi.Wikipedia.page.exists')
    @patch("program.classes.call_api.wikipediaapi.Wikipedia.page")
    def test_return_wikipedia_api(self, mock_url, mock_summary, mock_page, mock_exists):
        """Testing if the method only keep result with every wanted elements"""
        mock_exists = True
        if mock_page == mock_exists:
            url = mock_url.return_value = "https://fr.wikipedia.org/wiki/OpenClassrooms"
            summary = mock_summary.return_value = "OpenClassrooms est une école en ligne qui propose à ses membres des cours " \
                                    "certifiants et des parcours débouchant sur un métier d'avenir, " \
                                    "réalisés en interne, par des écoles, des universités, " \
                                    "ou encore par des entreprises partenaires comme Microsoft ou IBM. Jusqu'en 2018, " \
                                    "n'importe quel membre du site pouvait être auteur, via un outil nommé 'Course Lab'. " \
                                    "De nombreux cours sont issus de la communauté, mais ne sont plus mis en avant. " \
                                    "Initialement orientée autour de la programmation informatique, " \
                                    "la plate-forme couvre depuis 2013 des thématiques plus larges tels que le marketing, " \
                                    "l'entrepreneuriat et les sciences. " \
                                    "Créé en 1999 sous le nom de Site du Zéro, il se forme essentiellement sur la base " \
                                    "de contributions de bénévoles proposant des tutoriels vulgarisés avec un ton léger " \
                                    "portant sur des sujets informatiques divers. " \
                                    "À la suite du succès et de la fin des études des gérants, l'entreprise Simple IT, " \
                                    "renommée ensuite OpenClassrooms, est fondée dans le but de pérenniser le site. " \
                                    "Celle-ci base son modèle économique sur la délivrance de certifications payantes " \
                                    "et propose un abonnement pour être suivi par un mentor,. Suite à ces changements, " \
                                    "des utilisateurs créent un site web aux buts similaires, dont les auteurs et " \
                                    "l'association le gérant sont uniquement bénévoles et ne propose pas de " \
                                    "certifications (Zeste de Savoir). " \
                                    "En 2015, le site déclare compter 1 million de comptes depuis sa création, " \
                                    "ainsi qu'un trafic de 2,5 millions de visiteurs uniques par mois. La même année, " \
                                    "l'abonnement Premium est proposé gratuitement à tous les demandeurs d'emplois " \
                                    "français, en partenariat avec Pôle emploi et le gouvernement. " \
                                    "En 2016, Openclassrooms a commencé à mettre en place des parcours, " \
                                    "une suite de cours et d'exercices pratiques appelés 'projets', " \
                                    "donnant suite pour certaines de ces formations, à un diplôme reconnu par " \
                                    "l'État français. Un abonnement Premium Plus est requis pour pouvoir suivre " \
                                    "un parcours."

            index = summary.find(".", 200)
            place_history = summary[:index + 1]

            result = {'history': place_history,
                    'url': url}

            self.assertEqual(self.ca.call_api_wikipedia('OpenClassrooms'), result)


    @patch('program.classes.call_api.wikipediaapi.Wikipedia.page.exists')
    @patch("program.classes.call_api.wikipediaapi.Wikipedia.page")
    def test_no_return_wikipedia_api(self, mock_page, mock_exists):
        """Testing if the method only keep result with every wanted elements"""
        mock_exists = False
        if mock_page == mock_exists:
            result = False
            self.assertEqual(self.ca.call_api_wikipedia('openclassrooms'), result)



# test si pas les mots clefs reponse false
# test si pas de retour de l'api google maps ?

