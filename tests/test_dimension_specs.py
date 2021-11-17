import json

from druid_query.utils import druid_serealize
from druid_query.components import dimension_specs as dss
from druid_query.components import extraction_functions as efs

def test_json_conversion():
    ds = dss.Default('dim', 'out')
    generated = json.loads(json.dumps(ds, default=druid_serealize))
    expected = {
        'type': 'default',
        'dimension': 'dim',
        'outputName': 'out'
    }
    assert generated == expected

    ds = dss.Extraction('dim', 'out', efs.Partial('exp'))
    generated = json.loads(json.dumps(ds, default=druid_serealize))
    expected = {
        'type': 'extraction',
        'dimension': 'dim',
        'outputName': 'out',
        'extractionFn': {
            'type': 'partial',
            'expr': 'exp'
        }
    }
    assert generated == expected

    ds = dss.ListFiltered('dim', ['a', 'b'])
    generated = json.loads(json.dumps(ds, default=druid_serealize))
    expected = {
        'type': 'listFiltered',
        'delegate': 'dim',
        'values': ['a', 'b']
    }
    assert generated == expected

    ds = dss.RegexFiltered('dim', 'regpat')
    generated = json.loads(json.dumps(ds, default=druid_serealize))
    expected = {
        'type': 'regexFiltered',
        'delegate': 'dim',
        'pattern': 'regpat'
    }
    assert generated == expected

    ds = dss.PrefixFiltered('dim', 'pref')
    generated = json.loads(json.dumps(ds, default=druid_serealize))
    expected = {
        'type': 'prefixFiltered',
        'delegate': 'dim',
        'prefix': 'pref'
    }
    assert generated == expected

    ds = dss.Lookup('dim', 'out')
    generated = json.loads(json.dumps(ds, default=druid_serealize))
    expected = {
        'type': 'lookup',
        'dimension': 'dim',
        'outputName': 'out'
    }
    assert generated == expected
