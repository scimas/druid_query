from dataclasses import dataclass


@dataclass
class ToInclude:
    type: str


@dataclass
class All(ToInclude):
    pass


@dataclass
class Nothing(ToInclude):
    pass


@dataclass
class List(ToInclude):
    columns: list[str]
