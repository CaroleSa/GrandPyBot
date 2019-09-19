#! /usr/bin/env python3
# coding: UTF-8

from program.classes import parser as pa

class Test:
    def setup_method(self):
        self.new_parser = pa.Parser()

    def test_empty(self):
        results_empty = self.new_parser.get_place_searched("")
        assert results_empty == ""

    def test_space(self):
        results_space = self.new_parser.get_place_searched("    ")
        assert results_space == ""

    def test_lower(self):
        results_lower = self.new_parser.get_place_searched("Openclassrooms")
        assert results_lower == "openclassrooms"

    def test_no_symbols(self):
        results_no_symbols = self.new_parser.get_place_searched("saint-nazaire")
        assert results_no_symbols == "saint nazaire"

    def test_get_place(self):
        results_no_common_words = self.new_parser.get_place_searched("je cherche la mairie de caluire")
        assert results_no_common_words == "mairie caluire"

    def test_stop_words(self):
        results_stop_words = self.new_parser.get_place_searched("je cherche un lieu")
        assert results_stop_words == ""
