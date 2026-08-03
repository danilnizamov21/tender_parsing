import asyncio

from playwright.async_api import async_playwright

from config import B2B, BIDZAAR, ROSTENDER, ROSTORG, SiteConfig


async def browser(config: SiteConfig):
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        await page.goto(config.url)

        await config.prepare(page, config)
        await browser.close()


async def main():

    await asyncio.gather(
        browser(ROSTENDER), browser(B2B), browser(BIDZAAR), browser(ROSTORG)
    )


if __name__ == "__main__":
    asyncio.run(main())
