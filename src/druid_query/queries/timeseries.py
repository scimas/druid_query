from dataclasses import dataclass
from typing import Optional

from queries import NativeQuery


@dataclass
class Timeseries(NativeQuery):
    descending: Optional[bool] = None
    limit: Optional[int] = None

