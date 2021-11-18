import json

from druid_query.utils import druid_serealize
from druid_query.components import intervals

def test_json_conversion():
    intv = intervals.Interval('2021-01-01', '2021-01-02')
    generated = json.loads(json.dumps(intv, default=druid_serealize))
    expected = '2021-01-01/2021-01-02'
    assert generated == expected
