from dataclasses import dataclass
from typing import Optional

from .dimension_specs import DimensionSpec
from .extraction_functions import ExtractionFunction
from .search_query_specs import SearchQuerySpec
from .intervals import Interval


@dataclass
class Filter:
    type: str


@dataclass
class Selector(Filter):
    dimension: DimensionSpec
    value: str
    extraction_fn: Optional[ExtractionFunction] = None


@dataclass
class ColumnComparison(Filter):
    dimensions: list[DimensionSpec]


@dataclass
class Regex(Filter):
    dimension: DimensionSpec
    pattern: str
    extraction_fn: Optional[ExtractionFunction] = None


@dataclass
class And(Filter):
    fields: list[Filter]


@dataclass
class Or(Filter):
    fields: list[Filter]


@dataclass
class Not(Filter):
    field: Filter


@dataclass
class Javascript(Filter):
    dimension: DimensionSpec
    function: str
    extraction_fn: Optional[ExtractionFunction] = None


@dataclass
class Extraction(Filter):
    dimension: DimensionSpec
    value: str
    extraction_fn: ExtractionFunction


@dataclass
class Search(Filter):
    dimension: DimensionSpec
    query: SearchQuerySpec
    extraction_fn: Optional[ExtractionFunction] = None


@dataclass
class In(Filter):
    dimension: DimensionSpec
    values: list[str]


@dataclass
class Like(Filter):
    dimension: str
    pattern: str
    escape: Optional[str] = None
    extraction_fn: Optional[ExtractionFunction] = None


@dataclass
class Bound(Filter):
    dimension: str
    lower: Optional[str] = None
    upper: Optional[str] = None
    lower_strict: Optional[bool] = None
    upper_strict: Optional[bool] = None
    orderring: Optional[str] = None
    extraction_fn: Optional[ExtractionFunction] = None


@dataclass
class Interval(Filter):
    dimension: str
    intervals: list[Interval]
    extraction_fn: Optional[ExtractionFunction] = None


@dataclass
class Expression(Filter):
    expression: str


@dataclass
class TrueF(Filter):
    pass


@dataclass
class SpatialBound:
    type: str


@dataclass
class Rectangular(SpatialBound):
    min_coords: list[float]
    max_coords: list[float]


@dataclass
class Radius(SpatialBound):
    coords: list[float]
    radius: float


@dataclass
class Polygon(SpatialBound):
    abscissa: list[float]
    ordinate: list[float]


@dataclass
class Spatial(Filter):
    dimension: str
    bound: SpatialBound
