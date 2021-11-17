import json

from druid_query.utils import druid_serealize
from druid_query.components import search_query_specs as sqs

def test_json_conversion():
    sq = sqs.InsensitiveContains(2)
    generated = json.loads(json.dumps(sq, default=druid_serealize))
    expected = {
        'type': 'insensitiveContains',
        'value': 2
    }
    assert generated == expected

    sq = sqs.Fragment(True, ['a', 2])
    generated = json.loads(json.dumps(sq, default=druid_serealize))
    expected = {
        'type': 'fragment',
        'caseSensitive': True,
        'values': ['a', 2]
    }
    assert generated == expected

    sq = sqs.Contains(False, 'b')
    generated = json.loads(json.dumps(sq, default=druid_serealize))
    expected = {
        'type': 'contains',
        'caseSensitive': False,
        'value': 'b'
    }
    assert generated == expected

    sq = sqs.Regex('pat')
    generated = json.loads(json.dumps(sq, default=druid_serealize))
    expected = {
        'type': 'regex',
        'pattern': 'pat'
    }
    assert generated == expected
