from dataclasses import dataclass
from typing import Optional


@dataclass
class TopNMetricSpec:
    type: str


@dataclass
class Numeric(TopNMetricSpec):
    metric: str


@dataclass
class Dimension(TopNMetricSpec):
    ordering: Optional[str]
    previous_stop: Optional[str]


@dataclass
class Inverted(TopNMetricSpec):
    metric: TopNMetricSpec
