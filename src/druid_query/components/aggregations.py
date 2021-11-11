from dataclasses import dataclass
from typing import Optional

from .filters import Filter
from .dimension_specs import DimensionSpec

@dataclass
class Aggregator:
    type: str

@dataclass
class Count(Aggregator):
    name: str

@dataclass
class LongSum(Aggregator):
    name: str
    field_name: str

@dataclass
class DoubleSum(Aggregator):
    name: str
    field_name: str

@dataclass
class FloatSum(Aggregator):
    name: str
    field_name: str

@dataclass
class LongMin(Aggregator):
    name: str
    field_name: str

@dataclass
class DoubleMin(Aggregator):
    name: str
    field_name: str

@dataclass
class FloatMin(Aggregator):
    name: str
    field_name: str

@dataclass
class LongMax(Aggregator):
    name: str
    field_name: str

@dataclass
class DoubleMax(Aggregator):
    name: str
    field_name: str

@dataclass
class FloatMax(Aggregator):
    name: str
    field_name: str

@dataclass
class LongFirst(Aggregator):
    name: str
    field_name: str

@dataclass
class DoubleFirst(Aggregator):
    name: str
    field_name: str

@dataclass
class FloatFirst(Aggregator):
    name: str
    field_name: str

@dataclass
class StringFirst(Aggregator):
    name: str
    field_name: str
    max_string_bytes: int

@dataclass
class LongLast(Aggregator):
    name: str
    field_name: str

@dataclass
class DoubleLast(Aggregator):
    name: str
    field_name: str

@dataclass
class FloatLast(Aggregator):
    name: str
    field_name: str

@dataclass
class StringLast(Aggregator):
    name: str
    field_name: str
    max_string_bytes: int

@dataclass
class LongAny(Aggregator):
    name: str
    field_name: str

@dataclass
class DoubleAny(Aggregator):
    name: str
    field_name: str

@dataclass
class FloatAny(Aggregator):
    name: str
    field_name: str

@dataclass
class StringAny(Aggregator):
    name: str
    field_name: str
    max_string_bytes: int

@dataclass
class Javascript(Aggregator):
    name: str
    field_names: list[str]
    fn_aggregate: str
    fn_combine: str
    fn_reset: str

@dataclass
class Filtered(Aggregator):
    filter: Filter
    aggregator: Aggregator

@dataclass
class Grouping(Aggregator):
    name: str
    grouping: list[str]

@dataclass
class Cardinality(Aggregator):
    name: str
    fields: list[DimensionSpec]
    by_row: Optional[bool] = None
    round: Optional[bool] = None

@dataclass
class HyperUnique(Aggregator):
    name: str
    field_name: str
    is_input_hyper_unique: Optional[bool] = None
    round: Optional[bool] = None
