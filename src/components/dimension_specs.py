from dataclasses import dataclass
from typing import Optional, Union

from extraction_functions import ExtractionFunction
import lookups


@dataclass
class DimensionSpec:
    type: str


@dataclass
class Default(DimensionSpec):
    dimension: str
    output_name: str
    output_type: Optional[str] = None


@dataclass
class Extraction(DimensionSpec):
    dimension: str
    output_name: str
    extraction_fn: ExtractionFunction
    output_type: Optional[str] = None


@dataclass
class ListFiltered(DimensionSpec):
    delegate: DimensionSpec
    values: list[str]
    is_whitelist: Optional[bool] = None


@dataclass
class RegexFiltered(DimensionSpec):
    delegate: DimensionSpec
    pattern: str


@dataclass
class PrefixFiltered(DimensionSpec):
    delegate: DimensionSpec
    prefix: str


@dataclass
class Lookup(DimensionSpec):
    dimension: str
    output_name: str
    retain_missing_value: Optional[bool] = None
    replace_missing_value_with: Optional[Union[str, int, float]] = None
    lookup: Optional[lookups.Lookup] = None
    optimize: Optional[bool] = None
    name: Optional[str] = None
