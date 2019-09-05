#! /usr/bin/env python3
# coding: UTF-8


import program.call_api as ca

import urllib.request
from io import BytesIO
import json

def test_callapimaps(monkeypatch):

    def mockreturn(request):
        return results

    monkeypatch.setattr(urllib.request, 'urlopen', mockreturn)

    new_callapimaps = ca.CallApiMaps()
    results = new_callapimaps.get_place_coordonates("toulouse")

    assert ('Toulouse, France', 43.604652, 1.444209) == results

