import asyncio
from playwright.async_api import async_playwright
from typing import List

class PdfGenerator:
    def __init__(self, urls: List[str]):
        self.urls = urls

    async def _get_pdf_from_url(self, playwright, url):
        browser = await playwright.chromium.launch(headless=True)
        context = await browser.new_context()
        page = await context.new_page()
        await page.goto(url, wait_until="load", timeout=6000)
        await asyncio.sleep(2)  # Optional extra delay of 2 seconds
        pdf_content = await page.pdf(format="A4")  # Adjust options as needed
        await browser.close()
        return pdf_content

    async def generate_pdfs(self) -> List[bytes]:
        async with async_playwright() as playwright:
            pdfs = []
            for url in self.urls:
                pdf_content = await self._get_pdf_from_url(playwright, url)
                pdfs.append(pdf_content)
            return pdfs

    def main(self) -> List[bytes]:
        return asyncio.run(self.generate_pdfs())