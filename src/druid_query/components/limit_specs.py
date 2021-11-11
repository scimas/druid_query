from dataclasses import dataclass
from typing import Optional


@dataclass
class LimitSpec:
    type: str


@dataclass
class Default(LimitSpec):
    limit: Optional[int] = None
    offset: Optional[int] = None
    columns: Optional[list[LimitSpec]] = None


@dataclass
class OrderByColumnSpec(LimitSpec):
    dimension: str
    direction: str
    dimension_order: Optional[str]
