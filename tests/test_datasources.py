import json

from druid_query.utils import druid_serealize
from druid_query.components import data_sources as dss
from druid_query.components.intervals import Interval
from druid_query.queries import Scan

def test_json_conversion():
    ds = dss.Table('nm')
    generated = json.loads(json.dumps(ds, default=druid_serealize))
    expected = {
        'type': 'table',
        'name': 'nm'
    }
    assert generated == expected

    ds = dss.Lookup('lkp')
    generated = json.loads(json.dumps(ds, default=druid_serealize))
    expected = {
        'type': 'lookup',
        'lookup': 'lkp'
    }
    assert generated == expected

    ds = dss.Union(['tbl1', 'tbl2'])
    generated = json.loads(json.dumps(ds, default=druid_serealize))
    expected = {
        'type': 'union',
        'dataSources': ['tbl1', 'tbl2']
    }
    assert generated == expected

    ds = dss.Inline(['c1', 'c2'], [[1, 'r12'], [2, 'r22']])
    generated = json.loads(json.dumps(ds, default=druid_serealize))
    expected = {
        'type': 'inline',
        'columnNames': ['c1', 'c2'],
        'rows': [[1, 'r12'], [2, 'r22']]
    }
    assert generated == expected

    ds = dss.Query(Scan('tbl', [Interval('2021-01-01', '2021-01-02')]))
    generated = json.loads(json.dumps(ds, default=druid_serealize))
    expected = {
        'type': 'query',
        'query': {
            'queryType': 'scan',
            'dataSource': 'tbl',
            'intervals': ['2021-01-01/2021-01-02']
        }
    }
    assert generated == expected

    ds = dss.Join('tbl1', 'tbl2', 'rp', 'tbl1.a = tbl2.a', 'inner')
    generated = json.loads(json.dumps(ds, default=druid_serealize))
    expected = {
        'type': 'join',
        'left': 'tbl1',
        'right': 'tbl2',
        'rightPrefix': 'rp',
        'condition': 'tbl1.a = tbl2.a',
        'joinType': 'inner'
    }
    assert generated == expected
