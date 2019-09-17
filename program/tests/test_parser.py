#! /usr/bin/env python3
# coding: UTF-8

import program.parser as pa

def test_get_place_searched():
    new_parser = pa.Parser()
    results = new_parser.get_place_searched("Openclassrooms")
    assert results == "openclassrooms"

def test_get_place_searched():
    new_parser = pa.Parser()
    results = new_parser.get_place_searched("saint-nazaire")
    assert results == "saint nazaire"

def test_get_place_searched():
    new_parser = pa.Parser()
    results = new_parser.get_place_searched("je cherche la mairie de caluire")
    assert results == "mairie caluire"
