from typing import Union

from .dimension_specs import DimensionSpec

DruidNativeType = Union[str, int, float]

DruidSqlType = Union[str, int, float, bool]

Dimension = Union[DimensionSpec, str]
