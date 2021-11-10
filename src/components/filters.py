from dataclasses import dataclass
from typing import Optional

@dataclass
class Filter:
    type: str

@dataclass
class Selector(Filter):
    dimension: DimensionSpec
    value: str
    extraction_fn: Optional[ExtractionFunction]
