from dataclasses import dataclass


@dataclass
class Function:
    name: str
    description: str
    code: str


@dataclass
class Module:
    name: str
    functions: list[Function]
