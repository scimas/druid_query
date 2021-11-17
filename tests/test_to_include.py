import json

from druid_query.utils import druid_serealize
from druid_query.components import to_include as tnc

def test_json_conversion():
    ti = tnc.All()
    generated = json.loads(json.dumps(ti, default=druid_serealize))
    expected = {
        'type': 'all'
    }
    assert generated == expected

    ti = tnc.Nothing()
    generated = json.loads(json.dumps(ti, default=druid_serealize))
    expected = {
        'type': 'nothing'
    }
    assert generated == expected

    ti = tnc.List(['a', 'b'])
    generated = json.loads(json.dumps(ti, default=druid_serealize))
    expected = {
        'type': 'list',
        'columns': ['a', 'b']
    }
    assert generated == expected
