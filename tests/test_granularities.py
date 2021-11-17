import json

from druid_query.utils import druid_serealize
from druid_query.components import granularities as grn

def test_json_conversion():
    gn = grn.Duration(100)
    generated = json.loads(json.dumps(gn, default=druid_serealize))
    expected = {
        'type': 'duration',
        'duration': 100
    }
    assert generated == expected

    gn = grn.Period('PT1H')
    generated = json.loads(json.dumps(gn, default=druid_serealize))
    expected = {
        'type': 'period',
        'period': 'PT1H'
    }
    assert generated == expected
