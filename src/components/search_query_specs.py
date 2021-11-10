from dataclasses import dataclass
from typing import Union


@dataclass
class SearchQuerySpec:
    type: str


@dataclass
class InsensitiveContains(SearchQuerySpec):
    value: Union[str, int, float]


@dataclass
class Fragment(SearchQuerySpec):
    case_sensitive: bool
    values: list[Union[str, int, float]]


@dataclass
class Contains(SearchQuerySpec):
    case_sensitive: bool
    value: Union[str, int, float]


@dataclass
class Regex(SearchQuerySpec):
    pattern: str
