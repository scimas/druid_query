from dataclasses import dataclass

from .druid_types import DruidNativeType


@dataclass
class DataSource:
    type: str


@dataclass
class Table(DataSource):
    name: str


@dataclass
class Lookup(DataSource):
    lookup: str


@dataclass
class Union(DataSource):
    data_sources: list[str]


@dataclass
class Inline(DataSource):
    column_names: list[str]
    rows: list[list[DruidNativeType]]


@dataclass
class Query(DataSource):
    query: queries.Query


@dataclass
class Join(DataSource):
    left: DataSource
    right: DataSource
    right_prefix: str
    condition: str
    join_type: str
