import program.call_api as script

import urllib.request
from io import BytesIO
import json

def test_callapimaps(monkeypatch):
    results = [{
            "age": 84,
            "agreeableness": 0.74
          }]

    def mockreturn(request):
        return BytesIO(json.dumps(results).encode())

    monkeypatch.setattr(urllib.request, 'urlopen', mockreturn)
    assert script.CallApiWikipedia() == results
