from dataclasses import dataclass
from typing import Optional

from components.data_sources import DataSource
from components.virtual_columns import VirtualColumn
from components.context import Context
from components.intervals import Interval
from components.granularities import Granularity
from components.filters import Filter
from components.aggregations import Aggregator
from components.post_aggregations import PostAggregator
from src.components import aggregations

@dataclass
class NativeQuery:
    query_type: str
    data_source: DataSource
    intervals: list[Interval]
    granularity: Granularity
    filter: Optional[Filter]
    aggregations: Optional[list[Aggregator]]
    post_aggregations: Optional[list[PostAggregator]]
    virtual_columns: Optional[list[VirtualColumn]] = None
    context: Optional[Context] = None
