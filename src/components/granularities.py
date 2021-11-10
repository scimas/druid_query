from dataclasses import dataclass
from typing import Optional


@dataclass
class Granularity:
    type: str


@dataclass
class Simple(Granularity):
    name: str


@dataclass
class Duration(Granularity):
    duration: int
    origin: Optional[str] = None


@dataclass
class Period(Granularity):
    period: str
    origin: Optional[str] = None
    time_zone: Optional[str] = None
