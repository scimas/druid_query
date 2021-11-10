from dataclasses import dataclass
from typing import Optional, Union


@dataclass
class PostAggregator:
    type: str


@dataclass
class Arithmetic(PostAggregator):
    name: str
    fn: str
    fields: list[PostAggregator]
    ordering: Optional[str] = None


@dataclass
class FieldAccess(PostAggregator):
    name: str
    field_name: str


@dataclass
class FinalizingFieldAccess(PostAggregator):
    name: str
    field_name: str


@dataclass
class Constant(PostAggregator):
    name: str
    value: Union[str, int, float]


@dataclass
class LongGreatest(PostAggregator):
    name: str
    fields: list[PostAggregator]


@dataclass
class DoubleGreatest(PostAggregator):
    name: str
    fields: list[PostAggregator]


@dataclass
class LongLeast(PostAggregator):
    name: str
    fields: list[PostAggregator]


@dataclass
class DoubleLeast(PostAggregator):
    name: str
    fields: list[PostAggregator]


@dataclass
class Javascript(PostAggregator):
    name: str
    field_names: list[str]
    function: str


@dataclass
class HyperUniqueCardinality(PostAggregator):
    name: str
    field_name: str
