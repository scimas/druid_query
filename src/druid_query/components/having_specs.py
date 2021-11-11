from dataclasses import dataclass

from . import filters
from .druid_types import DruidNativeType


@dataclass
class HavingSpec:
    type: str


@dataclass
class Filter(HavingSpec):
    filter: filters.Filter


@dataclass
class EqualTo(HavingSpec):
    aggregation: str
    value: DruidNativeType


@dataclass
class GreaterThan(HavingSpec):
    aggregation: str
    value: DruidNativeType


@dataclass
class LessThan(HavingSpec):
    aggregation: str
    value: DruidNativeType


@dataclass
class DimSelector(HavingSpec):
    dimension: str
    value: DruidNativeType


@dataclass
class And(HavingSpec):
    having_specs: list[HavingSpec]


@dataclass
class Or(HavingSpec):
    having_specs: list[HavingSpec]


@dataclass
class Not(HavingSpec):
    having_spec: HavingSpec
