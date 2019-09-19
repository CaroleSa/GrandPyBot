#! /usr/bin/env python3
# coding: UTF-8

from program.classes import parser as pa

class Test:
    def setup_method(self):
        self.new_parser = pa.Parser()

    def test_lower(self):
        self.results_lower = self.new_parser.get_place_searched("Openclassrooms")
        assert self.results_lower == "openclassrooms"

    def test_no_symbols(self):
        self.results_no_symbols = self.new_parser.get_place_searched("saint-nazaire")
        assert self.results_no_symbols == "saint nazaire"

    def test_no_common_words(self):
        self.results_no_common_words = self.new_parser.get_place_searched("je cherche la mairie de caluire")
        assert self.results_no_common_words == "mairie caluire"
