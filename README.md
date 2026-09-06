# tender_parser

Сбор закупок с нескольких тендерных площадок: поиск по ключевым словам, разбор HTML и выгрузка в Excel.

Браузер открывается через [Playwright](https://playwright.dev/python/), карточки разбираются [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/) (`lxml`), результат пишется в `.xlsx`.

## Площадки

| Конфиг | Класс | Сайт |
|---|---|---|
| `ROSTENDER` | `RostenderSite` | [rostender.info](https://rostender.info/extsearch/advanced) |
| `BIDZAAR` | `BidzaarSite` | [bidzaar.com](https://bidzaar.com/app/requests/public/buy) |
| `B2B` | `B2BSite` | [b2b-center.ru](https://www.b2b-center.ru/market/) |
| `ROSTORG` | `RostorgSite` | [roseltorg.ru](https://www.roseltorg.ru/procedures/search) |

Сейчас точка входа (`main.py`) запускает **одну** площадку — `ROSTORG`. Остальные подключаются сменой импорта и класса в `main.py`.

Пагинация по всем страницам выдачи реализована для Rostender. У остальных `urls` пока не строит список страниц, в файл попадает первая выдача.

## Что собирается

Каждая карточка приводится к одной модели `Tender`:

| Поле | Смысл |
|---|---|
| `source` | Площадка (имя файла / источник) |
| `title` | Название |
| `url` | Ссылка |
| `price` | Начальная цена, если есть в вёрстке |
| `deadline` | Дата / срок |

Файл Excel: колонки «Источник», «Название», «Ссылка», «Стоимость», «Дата». Имя файла берётся из `output_filename` в конфиге, например `rostorg.xlsx` в корне проекта.

## Требования

- Python 3.12+

## Установка

Из корня репозитория:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```


## Настройка поиска

Ключевые слова и селекторы задаются в [`config.py`](config.py), не в командной строке.

Примеры полей `SiteConfig`:

- `url` — страница поиска
- `search` — строка в поисковом поле
- `exception_serch` — слова-исключения (есть у Rostender), иначе `None`
- `output_filename` — имя xlsx без расширения
- `search_input` / `search_button` / `exlude_input` — селекторы формы
- `parents_tag`, `title_tag`, `day_tag`, `cost_tag` и соответствующие `*_classname` — разбор карточки для универсального парсера

Чтобы сменить запрос, поправьте `search` у нужного конфига. Чтобы сменить площадку в запуске, в `main.py` укажите другой конфиг и класс, например:

```python
from config import ROSTENDER
from sites.rostender import RostenderSite

async def main():
    await browser(ROSTENDER)

# внутри browser():
site = RostenderSite(config)
```

Аналогично: `BIDZAAR` + `BidzaarSite`, `B2B` + `B2BSite`.

Браузер сейчас стартует с `headless=False` (видно окно). Для фона в `main.py` поставьте `headless=True`.

## Запуск

```bash
cd /path/to/parser
source venv/bin/activate
python main.py
```

Скрипт откроет Chromium, выполнит поиск, разберёт HTML и запишет xlsx. Первый прогон может занять заметное время из‑за пауз ожидания страницы.

## Как это устроено



1. `main` поднимает браузер и передаёт в раннер объект сайта (`RostorgSite` и т.д.).
2. `SiteRunner` открывает `settings.url`, вызывает `page_search`, снимает HTML.
3. `page_parse` собирает `list[Tender]`. Если `urls` вернул список адресов, раннер обходит их и дописывает строки.
4. `save_tenders` создаёт Excel.

Новая площадка: запись в `config.py` + класс в `sites/` с методами `page_search`, `urls`, `page_parse` (тот же контракт, что у существующих). Раннер менять не нужно.

