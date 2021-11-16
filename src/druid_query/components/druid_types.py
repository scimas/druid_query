from typing import Union

from .dimension_specs import DimensionSpec
from .granularities import NativeGranularity

DruidNativeType = Union[str, int, float]

DruidSqlType = Union[str, int, float, bool]

Dimension = Union[DimensionSpec, str]

Granularity = Union[NativeGranularity, str]
