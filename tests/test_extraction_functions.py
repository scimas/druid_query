import json

from druid_query.utils import druid_serealize
from druid_query.components import extraction_functions as efs
from druid_query.components import search_query_specs as sqs
from druid_query.components import lookups as lkps

def test_json_conversion():
    ef = efs.Regex('regpat')
    generated = json.loads(json.dumps(ef, default=druid_serealize))
    expected = {
        'type': 'regex',
        'expr': 'regpat'
    }
    assert generated == expected

    ef = efs.Partial('exp')
    generated = json.loads(json.dumps(ef, default=druid_serealize))
    expected = {
        'type': 'partial',
        'expr': 'exp'
    }
    assert generated == expected

    ef = efs.SearchQuery(sqs.InsensitiveContains('a'))
    generated = json.loads(json.dumps(ef, default=druid_serealize))
    expected = {
        'type': 'searchQuery',
        'query': {
            'type': 'insensitiveContains',
            'value': 'a'
        }
    }
    assert generated == expected

    ef = efs.Substring(2)
    generated = json.loads(json.dumps(ef, default=druid_serealize))
    expected = {
        'type': 'substring',
        'index': 2
    }
    assert generated == expected

    ef = efs.Strlen()
    generated = json.loads(json.dumps(ef, default=druid_serealize))
    expected = {
        'type': 'strlen'
    }
    assert generated == expected

    ef = efs.TimeFormat()
    generated = json.loads(json.dumps(ef, default=druid_serealize))
    expected = {
        'type': 'timeFormat'
    }
    assert generated == expected

    ef = efs.Time('<iso_format>', '<non_iso_format>', True)
    generated = json.loads(json.dumps(ef, default=druid_serealize))
    expected = {
        'type': 'time',
        'timeFormat': '<iso_format>',
        'resultFormat': '<non_iso_format>',
        'joda': True
    }
    assert generated == expected

    ef = efs.Javascript('fn')
    generated = json.loads(json.dumps(ef, default=druid_serealize))
    expected = {
        'type': 'javascript',
        'function': 'fn'
    }
    assert generated == expected

    ef = efs.RegisteredLookup('lkp')
    generated = json.loads(json.dumps(ef, default=druid_serealize))
    expected = {
        'type': 'registeredLookup',
        'lookup': 'lkp'
    }
    assert generated == expected

    ef = efs.Lookup(lkps.Map({'a': 'aval'}))
    generated = json.loads(json.dumps(ef, default=druid_serealize))
    expected = {
        'type': 'lookup',
        'lookup': {
            'type': 'map',
            'map': {'a': 'aval'}
        }
    }
    assert generated == expected

    ef = efs.Cascade([efs.Strlen(), efs.Strlen()])
    generated = json.loads(json.dumps(ef, default=druid_serealize))
    expected = {
        'type': 'cascade',
        'extractionFns': [
            {'type': 'strlen'}, {'type': 'strlen'}
        ]
    }
    assert generated == expected

    ef = efs.StringFormat('fmt')
    generated = json.loads(json.dumps(ef, default=druid_serealize))
    expected = {
        'type': 'stringFormat',
        'format': 'fmt'
    }
    assert generated == expected

    ef = efs.Upper()
    generated = json.loads(json.dumps(ef, default=druid_serealize))
    expected = {
        'type': 'upper'
    }
    assert generated == expected

    ef = efs.Lower()
    generated = json.loads(json.dumps(ef, default=druid_serealize))
    expected = {
        'type': 'lower'
    }
    assert generated == expected

    ef = efs.Bucket()
    generated = json.loads(json.dumps(ef, default=druid_serealize))
    expected = {
        'type': 'bucket'
    }
    assert generated == expected
