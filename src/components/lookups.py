from dataclasses import dataclass
from typing import Optional, Union


@dataclass
class Lookup:
    type: str


@dataclass
class Map(Lookup):
    map: dict[Union[str, int, float], Union[str, int, float]]
    injective: Optional[bool]
