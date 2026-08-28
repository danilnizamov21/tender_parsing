import asyncio

from playwright.async_api import async_playwright

from config import ROSTENDER
from runner import SiteRunner
from sites.rostender import RostenderSite


async def browser(config):
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()

        site = RostenderSite(config)
        runner = SiteRunner()
        await runner.run(site, page)

        await browser.close()


async def main():

    await browser(ROSTENDER)


if __name__ == "__main__":
    asyncio.run(main())
