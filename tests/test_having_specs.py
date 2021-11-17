import json

from druid_query.utils import druid_serealize
from druid_query.components import having_specs as hss
from druid_query.components import filters as flt


def test_json_conversion():
    hs = hss.Filter(flt.TrueF())
    generated = json.loads(json.dumps(hs, default=druid_serealize))
    expected = {
        'type': 'filter',
        'filter': {
            'type': 'true'
        }
    }
    assert generated == expected

    hs = hss.EqualTo('agg', 2)
    generated = json.loads(json.dumps(hs, default=druid_serealize))
    expected = {
        'type': 'equalTo',
        'aggregation': 'agg',
        'value': 2
    }
    assert generated == expected

    hs = hss.GreaterThan('agg', 2)
    generated = json.loads(json.dumps(hs, default=druid_serealize))
    expected = {
        'type': 'greaterThan',
        'aggregation': 'agg',
        'value': 2
    }
    assert generated == expected

    hs = hss.LessThan('agg', 2)
    generated = json.loads(json.dumps(hs, default=druid_serealize))
    expected = {
        'type': 'lessThan',
        'aggregation': 'agg',
        'value': 2
    }
    assert generated == expected

    hs = hss.DimSelector('dim', 2)
    generated = json.loads(json.dumps(hs, default=druid_serealize))
    expected = {
        'type': 'dimSelector',
        'dimension': 'dim',
        'value': 2
    }
    assert generated == expected

    hs = hss.And([hss.EqualTo('agg', 2), hss.EqualTo('agg', 2)])
    generated = json.loads(json.dumps(hs, default=druid_serealize))
    expected = {
        'type': 'and',
        'havingSpecs': [
            {'type': 'equalTo', 'aggregation': 'agg', 'value': 2},
            {'type': 'equalTo', 'aggregation': 'agg', 'value': 2}
        ]
    }
    assert generated == expected

    hs = hss.Or([hss.EqualTo('agg', 2), hss.EqualTo('agg', 2)])
    generated = json.loads(json.dumps(hs, default=druid_serealize))
    expected = {
        'type': 'or',
        'havingSpecs': [
            {'type': 'equalTo', 'aggregation': 'agg', 'value': 2},
            {'type': 'equalTo', 'aggregation': 'agg', 'value': 2}
        ]
    }
    assert generated == expected

    hs = hss.Not(hss.EqualTo('agg', 2))
    generated = json.loads(json.dumps(hs, default=druid_serealize))
    expected = {
        'type': 'not',
        'havingSpec': {'type': 'equalTo', 'aggregation': 'agg', 'value': 2}
    }
    assert generated == expected
