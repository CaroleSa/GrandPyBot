#! /usr/bin/env python3
# coding: UTF-8

""" Class TestParser """



# imports
from unittest import TestCase
from program.classes.parser import Parser



class TestParser(TestCase):
    """ Parser tests """

    def setUp(self):
        self.new_parser = Parser()

    def test_empty(self):
        """ test if not question : the empty string """
        results_empty = self.new_parser.get_place_searched("")
        self.assertEqual(results_empty, "")

    def test_space(self):
        """ test if not question : the spaces """
        results_space = self.new_parser.get_place_searched("    ")
        self.assertEqual(results_space, "")

    def test_lower(self):
        """ test delete uppercase """
        results_lower = self.new_parser.get_place_searched("Openclassrooms")
        self.assertEqual(results_lower, "openclassrooms")

    def test_no_symbols(self):
        """ test delete symbols """
        results_no_symbols = self.new_parser.get_place_searched("saint-nazaire")
        self.assertEqual(results_no_symbols, "saint nazaire")

    def test_get_place(self):
        """ test delete common words """
        results_no_common_words = self.new_parser.get_place_searched\
            ("je cherche la mairie de caluire")
        self.assertEqual(results_no_common_words, "mairie caluire")

    def test_stop_words(self):
        """ test delete common words """
        results_stop_all_words = self.new_parser.get_place_searched("je cherche un lieu")
        self.assertEqual(results_stop_all_words, "")
