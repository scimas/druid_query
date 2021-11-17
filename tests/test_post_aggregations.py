import json

from druid_query.utils import druid_serealize
from druid_query.components import post_aggregations as pas

def test_optional_mandatory_fields():
    assert pas.FieldAccess('field') == pas.FieldAccess('field', 'field')
    assert pas.FinalizingFieldAccess('field') == pas.FinalizingFieldAccess('field', 'field')
    assert pas.HyperUniqueCardinality('field') == pas.HyperUniqueCardinality('field', 'field')

def test_json_conversion():
    pa = pas.Arithmetic('nm', '+', [pas.Constant('const', 2), pas.Constant('const2', 3)])
    generated = json.loads(json.dumps(pa, default=druid_serealize))
    expected = {
        'type': 'arithmetic',
        'name': 'nm',
        'fn': '+',
        'fields': [
            {'type': 'constant', 'name': 'const', 'value': 2},
            {'type': 'constant', 'name': 'const2', 'value': 3}
        ]
    }
    assert generated == expected

    pa = pas.FieldAccess('field')
    generated = json.loads(json.dumps(pa, default=druid_serealize))
    expected = {
        'type': 'fieldAccess',
        'fieldName': 'field',
        'name': 'field'
    }
    assert generated == expected

    pa = pas.FinalizingFieldAccess('field')
    generated = json.loads(json.dumps(pa, default=druid_serealize))
    expected = {
        'type': 'finalizingFieldAccess',
        'fieldName': 'field',
        'name': 'field'
    }
    assert generated == expected

    pa = pas.Constant('nm', 2)
    generated = json.loads(json.dumps(pa, default=druid_serealize))
    expected = {
        'type': 'constant',
        'name': 'nm',
        'value': 2
    }
    assert generated == expected

    pa = pas.LongGreatest('nm', [pas.Constant('const', 2), pas.Constant('const2', 3)])
    generated = json.loads(json.dumps(pa, default=druid_serealize))
    expected = {
        'type': 'longGreatest',
        'name': 'nm',
        'fields': [
            {'type': 'constant', 'name': 'const', 'value': 2},
            {'type': 'constant', 'name': 'const2', 'value': 3}
        ]
    }
    assert generated == expected

    pa = pas.DoubleGreatest('nm', [pas.Constant('const', 2), pas.Constant('const2', 3)])
    generated = json.loads(json.dumps(pa, default=druid_serealize))
    expected = {
        'type': 'doubleGreatest',
        'name': 'nm',
        'fields': [
            {'type': 'constant', 'name': 'const', 'value': 2},
            {'type': 'constant', 'name': 'const2', 'value': 3}
        ]
    }
    assert generated == expected

    pa = pas.LongLeast('nm', [pas.Constant('const', 2), pas.Constant('const2', 3)])
    generated = json.loads(json.dumps(pa, default=druid_serealize))
    expected = {
        'type': 'longLeast',
        'name': 'nm',
        'fields': [
            {'type': 'constant', 'name': 'const', 'value': 2},
            {'type': 'constant', 'name': 'const2', 'value': 3}
        ]
    }
    assert generated == expected

    pa = pas.DoubleLeast('nm', [pas.Constant('const', 2), pas.Constant('const2', 3)])
    generated = json.loads(json.dumps(pa, default=druid_serealize))
    expected = {
        'type': 'doubleLeast',
        'name': 'nm',
        'fields': [
            {'type': 'constant', 'name': 'const', 'value': 2},
            {'type': 'constant', 'name': 'const2', 'value': 3}
        ]
    }
    assert generated == expected

    pa = pas.Javascript('nm', ['f1', 'f2'], 'fn')
    generated = json.loads(json.dumps(pa, default=druid_serealize))
    expected = {
        'type': 'javascript',
        'name': 'nm',
        'fieldNames': ['f1', 'f2'],
        'function': 'fn'
    }
    assert generated == expected

    pa = pas.HyperUniqueCardinality('field')
    generated = json.loads(json.dumps(pa, default=druid_serealize))
    expected = {
        'type': 'hyperUniqueCardinality',
        'fieldName': 'field',
        'name': 'field'
    }
    assert generated == expected
