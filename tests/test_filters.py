import json

from druid_query.utils import druid_serealize
from druid_query.components import filters as flt
from druid_query.components import extraction_functions as efs
from druid_query.components import search_query_specs as sqs
from druid_query.components import intervals

def test_json_conversions():
    fl = flt.Selector('dim', 'val')
    generated = json.loads(json.dumps(fl, default=druid_serealize))
    expected = {
        'type': 'selector',
        'dimension': 'dim',
        'value': 'val'
    }
    assert generated == expected

    fl = flt.ColumnComparison(['dim1', 'dim2'])
    generated = json.loads(json.dumps(fl, default=druid_serealize))
    expected = {
        'type': 'columnComparison',
        'dimensions': ['dim1', 'dim2']
    }
    assert generated == expected

    fl = flt.Regex('dim', 'pat')
    generated = json.loads(json.dumps(fl, default=druid_serealize))
    expected = {
        'type': 'regex',
        'dimension': 'dim',
        'pattern': 'pat'
    }
    assert generated == expected

    fl = flt.And([flt.TrueF(), flt.TrueF()])
    generated = json.loads(json.dumps(fl, default=druid_serealize))
    expected = {
        'type': 'and',
        'fields': [{'type': 'true'}, {'type': 'true'}]
    }
    assert generated == expected

    fl = flt.Or([flt.TrueF(), flt.TrueF()])
    generated = json.loads(json.dumps(fl, default=druid_serealize))
    expected = {
        'type': 'or',
        'fields': [{'type': 'true'}, {'type': 'true'}]
    }
    assert generated == expected

    fl = flt.Not(flt.TrueF())
    generated = json.loads(json.dumps(fl, default=druid_serealize))
    expected = {
        'type': 'not',
        'field': {'type': 'true'}
    }
    assert generated == expected

    fl = flt.Javascript('dim', 'fn')
    generated = json.loads(json.dumps(fl, default=druid_serealize))
    expected = {
        'type': 'javascript',
        'dimension': 'dim',
        'function': 'fn'
    }
    assert generated == expected

    fl = flt.Extraction('dim', 'val', efs.Bucket())
    generated = json.loads(json.dumps(fl, default=druid_serealize))
    expected = {
        'type': 'extraction',
        'dimension': 'dim',
        'value': 'val',
        'extractionFn': {'type': 'bucket'}
    }
    assert generated == expected

    fl = flt.Search('dim', sqs.InsensitiveContains('a'))
    generated = json.loads(json.dumps(fl, default=druid_serealize))
    expected = {
        'type': 'search',
        'dimension': 'dim',
        'query': {
            'type': 'insensitiveContains',
            'value': 'a'
        }
    }
    assert generated == expected

    fl = flt.In('dim', ['a', 'b'])
    generated = json.loads(json.dumps(fl, default=druid_serealize))
    expected = {
        'type': 'in',
        'dimension': 'dim',
        'values': ['a', 'b']
    }
    assert generated == expected

    fl = flt.Like('dim', 'pat')
    generated = json.loads(json.dumps(fl, default=druid_serealize))
    expected = {
        'type': 'like',
        'dimension': 'dim',
        'pattern': 'pat'
    }
    assert generated == expected

    fl = flt.Bound('dim')
    generated = json.loads(json.dumps(fl, default=druid_serealize))
    expected = {
        'type': 'bound',
        'dimension': 'dim'
    }
    assert generated == expected

    fl = flt.Interval('dim', [intervals.Interval('2021-01-01', '2021-01-02')])
    generated = json.loads(json.dumps(fl, default=druid_serealize))
    expected = {
        'type': 'interval',
        'dimension': 'dim',
        'intervals': ['2021-01-01/2021-01-02']
    }
    assert generated == expected

    fl = flt.Expression('exp')
    generated = json.loads(json.dumps(fl, default=druid_serealize))
    expected = {
        'type': 'expression',
        'expression': 'exp'
    }
    assert generated == expected

    fl = flt.TrueF()
    generated = json.loads(json.dumps(fl, default=druid_serealize))
    expected = {'type': 'true'}
    assert generated == expected

    # fl = flt.Rectangular([1.0, 2.0], [2.0, 3.0])
    # generated = json.loads(json.dumps(fl, default=druid_serealize))
    # expected = {
    #     'type': 'rectangular',
    #     'minCoords': [1.0, 2.0],
    #     'maxCoords': [2.0, 3.0],
    # }
    # assert generated == expected

    # fl = flt.Radius([1.0, 2.0], 5.0)
    # generated = json.loads(json.dumps(fl, default=druid_serealize))
    # expected = {
    #     'type': 'radius',
    #     'coords': [1.0, 2.0],
    #     'radius': 5.0
    # }
    # assert generated == expected

    # fl = flt.Polygon([1.0, 2.0], [2.0, 3.0])
    # generated = json.loads(json.dumps(fl, default=druid_serealize))
    # expected = {
    #     'type': 'polygon',
    #     'abscissa': [1.0, 2.0],
    #     'ordinate': [2.0, 3.0]
    # }
    # assert generated == expected

    fl = flt.Spatial('dim', flt.Radius([1.0, 2.0], 5.0))
    generated = json.loads(json.dumps(fl, default=druid_serealize))
    expected = {
        'type': 'spatial',
        'dimension': 'dim',
        'bound': {
            'type': 'radius',
            'coords': [1.0, 2.0],
            'radius': 5.0
        }
    }
    assert generated == expected
