import json

from druid_query.utils import druid_serealize
from druid_query.components import limit_specs as lss

def test_json_conversion():
    ls = lss.Default()
    generated = json.loads(json.dumps(ls, default=druid_serealize))
    expected = {
        'type': 'default'
    }
    assert generated == expected
