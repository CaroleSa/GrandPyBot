#! /usr/bin/env python3
# coding: UTF-8

from unittest import TestCase
from program.classes import parser as pa

class TestParser(TestCase):
    def setUp(self):
        self.new_parser = pa.Parser()

    def test_empty(self):
        results_empty = self.new_parser.get_place_searched("")
        self.assertEqual(results_empty, "")

    def test_space(self):
        results_space = self.new_parser.get_place_searched("    ")
        self.assertEqual(results_space, "")

    def test_lower(self):
        results_lower = self.new_parser.get_place_searched("Openclassrooms")
        self.assertEqual(results_lower, "openclassrooms")

    def test_no_symbols(self):
        results_no_symbols = self.new_parser.get_place_searched("saint-nazaire")
        self.assertEqual(results_no_symbols, "saint nazaire")

    def test_get_place(self):
        results_no_common_words = self.new_parser.get_place_searched("je cherche la mairie de caluire")
        self.assertEqual(results_no_common_words, "mairie caluire")

    def test_stop_words(self):
        results_stop_words = self.new_parser.get_place_searched("je cherche un lieu")
        self.assertEqual(results_stop_words, "")

unittest.main()