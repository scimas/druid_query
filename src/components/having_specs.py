from dataclasses import dataclass
from typing import Union

import filters


@dataclass
class HavingSpec:
    type: str


@dataclass
class Filter(HavingSpec):
    filter: filters.Filter


@dataclass
class EqualTo(HavingSpec):
    aggregation: str
    value: Union[str, int, float]


@dataclass
class GreaterThan(HavingSpec):
    aggregation: str
    value: Union[str, int, float]


@dataclass
class LessThan(HavingSpec):
    aggregation: str
    value: Union[str, int, float]


@dataclass
class DimSelector(HavingSpec):
    dimension: str
    value: Union[str, int, float]


@dataclass
class And(HavingSpec):
    having_specs: list[HavingSpec]


@dataclass
class Or(HavingSpec):
    having_specs: list[HavingSpec]


@dataclass
class Not(HavingSpec):
    having_spec: HavingSpec
