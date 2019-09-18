#! /usr/bin/env python3
# coding: UTF-8

from program.classes import parser as pa

class Test:
    def setup_method(self):
        new_parser = pa.Parser()
        self.results_lower = new_parser.get_place_searched("Openclassrooms")
        self.results_no_symbols = new_parser.get_place_searched("saint-nazaire")
        self.results_no_common_words = new_parser.get_place_searched("je cherche la mairie de caluire")

    def test_lower(self):
        assert self.results_lower == "openclassrooms"

    def test_no_symbols(self):
        assert self.results_no_symbols == "saint nazaire"

    def test_no_common_words(self):
        assert self.results_no_common_words == "mairie caluire"
