from dataclasses import dataclass
from typing import Optional

from druid_types import DruidNativeType


@dataclass
class Lookup:
    type: str


@dataclass
class Map(Lookup):
    map: dict[DruidNativeType, DruidNativeType]
    injective: Optional[bool]
