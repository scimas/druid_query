from dataclasses import dataclass

from druid_types import DruidNativeType


@dataclass
class SearchQuerySpec:
    type: str


@dataclass
class InsensitiveContains(SearchQuerySpec):
    value: DruidNativeType


@dataclass
class Fragment(SearchQuerySpec):
    case_sensitive: bool
    values: list[DruidNativeType]


@dataclass
class Contains(SearchQuerySpec):
    case_sensitive: bool
    value: DruidNativeType


@dataclass
class Regex(SearchQuerySpec):
    pattern: str
