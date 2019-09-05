#! /usr/bin/env python3
# coding: UTF-8

import program.parser as p

def test_get_place_searched():
    new_parser = p.Parser()
    results = new_parser.get_place_searched("je recherche Openclassrooms")
    assert results == ["openclassrooms"]
