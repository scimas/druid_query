import json

from druid_query.utils import druid_serealize
from druid_query.components import topn_metric_specs as tms

def test_json_conversion():
    tm = tms.Numeric('met')
    generated = json.loads(json.dumps(tm, default=druid_serealize))
    expected = {
        'type': 'numeric',
        'metric': 'met'
    }
    assert generated == expected

    tm = tms.Dimension()
    generated = json.loads(json.dumps(tm, default=druid_serealize))
    expected = {
        'type': 'dimension'
    }
    assert generated == expected

    tm = tms.Inverted(tms.Dimension())
    generated = json.loads(json.dumps(tm, default=druid_serealize))
    expected = {
        'type': 'inverted',
        'metric': {
            'type': 'dimension'
        }
    }
    assert generated == expected
