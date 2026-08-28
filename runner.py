from playwright.async_api import Page

from browser.actions import get_html
from storage.excel import save_tenders


class SiteRunner:
    async def run(self, site, page: Page) -> None:

        await page.goto(site.url)
        await site.search(page)

        html = await get_html(page)

        rows = list(site.parse(html))
        urls = site.urls(page.url, html)
        if urls:
            for url in urls:
                await page.goto(url)
                html = await get_html(page)
                rows.extend(site.page_parse(html))
        path = f"{site.settings.output_filename}.xlsx"
        save_tenders(path, rows)
