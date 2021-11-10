from dataclasses import dataclass
from typing import Optional, Union

from search_query_specs import SearchQuerySpec
from granularities import Granularity
from lookups import Lookup


@dataclass
class ExtractionFunction:
    type: str


@dataclass
class Regex(ExtractionFunction):
    expr: str
    index: Optional[int] = None
    replace_missing_value: Optional[bool] = None
    replace_missing_value_with: Optional[Union[str, int, float]] = None


@dataclass
class Partial(ExtractionFunction):
    expr: str


@dataclass
class SearchQuery(ExtractionFunction):
    query: SearchQuerySpec


@dataclass
class Substring(ExtractionFunction):
    index: int
    length: Optional[int] = None


@dataclass
class Strlen(ExtractionFunction):
    pass


@dataclass
class TimeFormat(ExtractionFunction):
    format: Optional[str] = None
    time_zone: Optional[str] = None
    locale: Optional[str] = None
    granularity: Optional[Granularity] = None
    as_millis: Optional[bool] = None


@dataclass
class Time(ExtractionFunction):
    time_format: str
    result_format: str
    joda: bool


@dataclass
class Javascript(ExtractionFunction):
    function: str
    injective: Optional[bool]


@dataclass
class RegisteredLookup(ExtractionFunction):
    lookup: str
    retain_missing_value: Optional[bool] = None
    replace_missing_value_with: Optional[Union[str, int, float]] = None
    injective: Optional[bool] = None
    optimize: Optional[bool] = None


@dataclass
class Lookup(ExtractionFunction):
    lookup: Lookup
    retain_missing_value: Optional[bool] = None
    replace_missing_value_with: Optional[Union[str, int, float]] = None
    injective: Optional[bool] = None
    optiomize: Optional[bool] = None


@dataclass
class Cascade(ExtractionFunction):
    extraction_fns: list[ExtractionFunction]


@dataclass
class StringFormat(ExtractionFunction):
    format: str
    null_handling: Optional[str] = None


@dataclass
class Upper(ExtractionFunction):
    locale: Optional[str] = None


@dataclass
class Lower(ExtractionFunction):
    locale: Optional[str] = None


@dataclass
class Bucket(ExtractionFunction):
    size: Optional[int] = None
    offset: Optional[int] = None
