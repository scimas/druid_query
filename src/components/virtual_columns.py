from dataclasses import dataclass
from typing import Optional


@dataclass
class VirtualColumn:
    type: str


@dataclass
class Expression(VirtualColumn):
    name: str
    expression: str
    output_type: Optional[str]
