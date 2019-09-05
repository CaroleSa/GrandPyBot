#! /usr/bin/env python3
# coding: UTF-8


import program.call_api as ca

import urllib.request
from io import BytesIO
import json

def test_callapimaps(monkeypatch):
    results = [{
            "lat": 48.8,
            "lng": 2.35
          }]

    def mockreturn(request):
        return results

    monkeypatch.setattr(urllib.request, 'urlopen', mockreturn)

    new_callapimaps = ca.CallApiMaps()
    longitude = new_callapimaps.longitude
    latitude = new_callapimaps.latitude
    assert [{"lat": latitude, "lng": longitude}] == results
