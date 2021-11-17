import json

from druid_query.utils import druid_serealize
from druid_query.components import virtual_columns as vcs

def test_json_conversion():
    vc = vcs.Expression('nm', 'exp')
    generated = json.loads(json.dumps(vc, default=druid_serealize))
    expected = {
        'type': 'expression',
        'name': 'nm',
        'expression': 'exp'
    }
    assert generated == expected
