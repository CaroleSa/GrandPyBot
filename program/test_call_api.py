#! /usr/bin/env python3
# coding: UTF-8



import urllib.request
from io import BytesIO
import json

import program.call_api as ca


def test_get_place_history():
    new_call_api_wiki = ca.CallApiWikipedia()
    results = new_call_api_wiki.get_place_history("Toulouse")
    assert results[0:24] == "Toulouse est une commune"


def test_get_place_coordonates(monkeypatch):
    results = ('Toulouse, France', 43.604652, 1.444209)

    def mockreturn(request):
        return BytesIO(json.dumps(results).encode())

    monkeypatch.setattr(urllib.request, 'urlopen', mockreturn)

    new_callapimaps = ca.CallApiMaps()
    result = new_callapimaps.get_place_coordonates("toulouse")

    assert result == results
