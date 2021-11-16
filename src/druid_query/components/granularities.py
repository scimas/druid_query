from dataclasses import dataclass
from typing import Optional


@dataclass
class NativeGranularity:
    pass


@dataclass
class Duration(NativeGranularity):
    duration: int
    origin: Optional[str] = None

    def __post_init__(self):
        self.type = 'duration'


@dataclass
class Period(NativeGranularity):
    period: str
    origin: Optional[str] = None
    time_zone: Optional[str] = None

    def __post_init__(self):
        self.type = 'period'
