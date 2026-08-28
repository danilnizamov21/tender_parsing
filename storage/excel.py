from openpyxl import Workbook

from domain.models import Tender

HEADERS = ("Источник", "Название", "ССылка", "Стоимость", "Дата")


def save_tenders(path: str, rows: list[Tender]) -> None:
    """Функция сохранения данных парсеров в xlsx документ. Данные распределены по заголовкам(HEADERS)"""
    wb = Workbook()
    ws = wb.active
    ws.title = "Тендеры"
    ws.append(list(HEADERS))
    for r in rows:
        ws.append([r.source, r.title, r.url, r.price or "", r.deadline or ""])
    wb.save(path)
