import json

from druid_query.utils import druid_serealize
from druid_query.components import lookups as lks

def test_json_conversion():
    lk = lks.Map({'a': 'b'})
    generated = json.loads(json.dumps(lk, default=druid_serealize))
    expected = {
        'type': 'map',
        'map': {'a': 'b'}
    }
    assert generated == expected
