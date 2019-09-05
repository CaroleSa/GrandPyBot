#! /usr/bin/env python3
# coding: UTF-8


import program.call_api as ca
import urllib.request
from io import BytesIO
import json


def test_get_place_history():
    new_call_api_wiki = ca.CallApiWikipedia()
    results = new_call_api_wiki.get_place_history("Toulouse")
    assert results[0:24] == "Toulouse est une commune"


"""def test_callapimaps(monkeypatch):

    def mockreturn(request):
        return results

    monkeypatch.setattr(urllib.request, 'urlopen', mockreturn)

    new_callapimaps = ca.CallApiMaps()
    results = new_callapimaps.get_place_coordonates("toulouse")

    assert ('Toulouse, France', 43.604652, 1.444209) == results"""

