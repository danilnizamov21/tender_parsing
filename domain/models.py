from dataclasses import dataclass


@dataclass
class Tender:  # список который будет возвращать каждый парсер
    source: str
    title: str
    url: str
    price: str | None
    deadline: str | None
