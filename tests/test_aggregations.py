import json

from druid_query.components import aggregations as aggs
from druid_query.utils import druid_serealize


def test_optional_mandatory_fields():
    """
        Some fields are mandatory on Druid side but can have convinient default
        values on this client library side. Make sure they are being filled out
        properly.
    """
    assert aggs.LongSum('abc') == aggs.LongSum('abc', 'abc')
    assert aggs.DoubleSum('abc') == aggs.DoubleSum('abc', 'abc')
    assert aggs.FloatSum('abc') == aggs.FloatSum('abc', 'abc')
    assert aggs.LongMin('abc') == aggs.LongMin('abc', 'abc')
    assert aggs.DoubleMin('abc') == aggs.DoubleMin('abc', 'abc')
    assert aggs.FloatMin('abc') == aggs.FloatMin('abc', 'abc')
    assert aggs.LongMax('abc') == aggs.LongMax('abc', 'abc')
    assert aggs.DoubleMax('abc') == aggs.DoubleMax('abc', 'abc')
    assert aggs.FloatMax('abc') == aggs.FloatMax('abc', 'abc')
    assert aggs.LongFirst('abc') == aggs.LongFirst('abc', 'abc')
    assert aggs.DoubleFirst('abc') == aggs.DoubleFirst('abc', 'abc')
    assert aggs.FloatFirst('abc') == aggs.FloatFirst('abc', 'abc')
    assert aggs.StringFirst('abc') == aggs.StringFirst('abc', 'abc')
    assert aggs.LongLast('abc') == aggs.LongLast('abc', 'abc')
    assert aggs.DoubleLast('abc') == aggs.DoubleLast('abc', 'abc')
    assert aggs.FloatLast('abc') == aggs.FloatLast('abc', 'abc')
    assert aggs.StringLast('abc') == aggs.StringLast('abc', 'abc')
    assert aggs.LongAny('abc') == aggs.LongAny('abc', 'abc')
    assert aggs.DoubleAny('abc') == aggs.DoubleAny('abc', 'abc')
    assert aggs.FloatAny('abc') == aggs.FloatAny('abc', 'abc')
    assert aggs.StringAny('abc') == aggs.StringAny('abc', 'abc')
    assert aggs.HyperUnique('abc') == aggs.HyperUnique('abc', 'abc')


def test_json_conversion():
    ag = aggs.Count('nm')
    generated = json.loads(json.dumps(ag, default=druid_serealize))
    expected = {
        'type': 'count',
        'name': 'nm'
    }
    assert generated == expected

    ag_constrs = [
        aggs.LongSum, aggs.DoubleSum, aggs.FloatSum, aggs.LongMin, aggs.DoubleMin, aggs.FloatMin,
        aggs.LongMax, aggs.DoubleMax, aggs.FloatMax, aggs.LongFirst, aggs.DoubleFirst, aggs.FloatFirst,
        aggs.StringFirst, aggs.LongLast, aggs.DoubleLast, aggs.FloatLast, aggs.StringLast, aggs.LongAny,
        aggs.DoubleAny, aggs.FloatAny, aggs.StringAny, aggs.HyperUnique
    ]
    for ag_constr in ag_constrs:
        ag = ag_constr('field', 'nm')
        generated = json.loads(json.dumps(ag, default=druid_serealize))
        expected = {'type': ag.type, 'name': ag.name,
                    'fieldName': ag.field_name}
        assert generated == expected, f'for {ag_constr}'

    ag = aggs.Javascript('nm', ['f1', 'f2'], 'aggregate', 'combine', 'reset')
    generated = json.loads(json.dumps(ag, default=druid_serealize))
    expected = {
        'type': 'javascript',
        'name': 'nm',
        'fieldNames': ['f1', 'f2'],
        'fnAggregate': 'aggregate',
        'fnCombine': 'combine',
        'fnReset': 'reset'
    }
    assert generated == expected

    ag = aggs.Grouping('nm', ['g1', 'g2'])
    generated = json.loads(json.dumps(ag, default=druid_serealize))
    expected = {
        'type': 'grouping',
        'name': 'nm',
        'grouping': ['g1', 'g2']
    }
    assert generated == expected

    ag = aggs.Cardinality('nm', ['f1', 'f2'])
    generated = json.loads(json.dumps(ag, default=druid_serealize))
    expected = {
        'type': 'cardinality',
        'name': 'nm',
        'fields': ['f1', 'f2']
    }
    assert generated == expected

    ag = aggs.HyperUnique('field', 'nm')
    generated = json.loads(json.dumps(ag, default=druid_serealize))
    expected = {
        'type': 'hyperUnique',
        'name': 'nm',
        'fieldName': 'field'
    }
    assert generated == expected
