from dataclasses import dataclass
from typing import Optional


@dataclass
class Granularity:
    pass


@dataclass
class Simple(Granularity):
    name: str

    def __post_init__(self):
        self.type = 'simple'


@dataclass
class Duration(Granularity):
    duration: int
    origin: Optional[str] = None

    def __post_init__(self):
        self.type = 'duration'


@dataclass
class Period(Granularity):
    period: str
    origin: Optional[str] = None
    time_zone: Optional[str] = None

    def __post_init__(self):
        self.type = 'period'
