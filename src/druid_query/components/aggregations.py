from dataclasses import dataclass, field
from typing import Optional

from .filters import Filter
from .dimension_specs import DimensionSpec


@dataclass
class Aggregator:
    pass


@dataclass
class Count(Aggregator):
    name: str

    def __post_init__(self):
        self.type = 'count'


@dataclass
class LongSum(Aggregator):
    name: str
    field_name: str

    def __post_init__(self):
        self.type = 'longSum'


@dataclass
class DoubleSum(Aggregator):
    name: str
    field_name: str

    def __post_init__(self):
        self.type = 'doubleSum'


@dataclass
class FloatSum(Aggregator):
    name: str
    field_name: str

    def __post_init__(self):
        self.type = 'floatSum'


@dataclass
class LongMin(Aggregator):
    name: str
    field_name: str

    def __post_init__(self):
        self.type = 'longMin'


@dataclass
class DoubleMin(Aggregator):
    name: str
    field_name: str

    def __post_init__(self):
        self.type = 'doubleMin'


@dataclass
class FloatMin(Aggregator):
    name: str
    field_name: str

    def __post_init__(self):
        self.type = 'floatMin'


@dataclass
class LongMax(Aggregator):
    name: str
    field_name: str

    def __post_init__(self):
        self.type = 'longMax'


@dataclass
class DoubleMax(Aggregator):
    name: str
    field_name: str

    def __post_init__(self):
        self.type = 'doubleMax'


@dataclass
class FloatMax(Aggregator):
    name: str
    field_name: str

    def __post_init__(self):
        self.type = 'floatMax'


@dataclass
class LongFirst(Aggregator):
    name: str
    field_name: str

    def __post_init__(self):
        self.type = 'longFirst'


@dataclass
class DoubleFirst(Aggregator):
    name: str
    field_name: str

    def __post_init__(self):
        self.type = 'doubleFirst'


@dataclass
class FloatFirst(Aggregator):
    name: str
    field_name: str

    def __post_init__(self):
        self.type = 'floatFirst'


@dataclass
class StringFirst(Aggregator):
    name: str
    field_name: str
    max_string_bytes: Optional[int] = None

    def __post_init__(self):
        self.type = 'stringFirst'


@dataclass
class LongLast(Aggregator):
    name: str
    field_name: str

    def __post_init__(self):
        self.type = 'longLast'


@dataclass
class DoubleLast(Aggregator):
    name: str
    field_name: str

    def __post_init__(self):
        self.type = 'doubleLast'


@dataclass
class FloatLast(Aggregator):
    name: str
    field_name: str

    def __post_init__(self):
        self.type = 'floatLast'


@dataclass
class StringLast(Aggregator):
    name: str
    field_name: str
    max_string_bytes: Optional[int] = None

    def __post_init__(self):
        self.type = 'stringLast'


@dataclass
class LongAny(Aggregator):
    name: str
    field_name: str

    def __post_init__(self):
        self.type = 'longAny'


@dataclass
class DoubleAny(Aggregator):
    name: str
    field_name: str

    def __post_init__(self):
        self.type = 'doubleAny'


@dataclass
class FloatAny(Aggregator):
    name: str
    field_name: str

    def __post_init__(self):
        self.type = 'floatAny'


@dataclass
class StringAny(Aggregator):
    name: str
    field_name: str
    max_string_bytes: Optional[int] = None

    def __post_init__(self):
        self.type = 'stringAny'


@dataclass
class Javascript(Aggregator):
    name: str
    field_names: list[str]
    fn_aggregate: str
    fn_combine: str
    fn_reset: str

    def __post_init__(self):
        self.type = 'javascript'


@dataclass
class Filtered(Aggregator):
    filter: Filter
    aggregator: Aggregator

    def __post_init__(self):
        self.type = 'filtered'


@dataclass
class Grouping(Aggregator):
    name: str
    grouping: list[str]

    def __post_init__(self):
        self.type = 'grouping'


@dataclass
class Cardinality(Aggregator):
    name: str
    fields: list[DimensionSpec]
    by_row: Optional[bool] = None
    round: Optional[bool] = None

    def __post_init__(self):
        self.type = 'cardinality'


@dataclass
class HyperUnique(Aggregator):
    name: str
    field_name: str
    is_input_hyper_unique: Optional[bool] = None
    round: Optional[bool] = None

    def __post_init__(self):
        self.type = 'hyperUnique'
