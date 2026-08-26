from dataclasses import dataclass


@dataclass
class Tender:
    source: str
    title: str
    url: str
    price: str | None
    deadline: str | None
