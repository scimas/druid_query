from dataclasses import dataclass
from typing import Optional


@dataclass
class LimitSpec:
    pass


@dataclass
class Default(LimitSpec):
    limit: Optional[int] = None
    offset: Optional[int] = None
    columns: Optional[list[LimitSpec]] = None

    def __post_init__(self):
        self.type = 'default'


@dataclass
class OrderByColumnSpec(LimitSpec):
    dimension: str
    direction: str
    dimension_order: Optional[str]

    def __post_init__(self):
        self.type = 'orderByColumnSpec'
