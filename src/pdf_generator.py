# import os
# import base64
# import json
# import time
# from io import BytesIO
# from typing import List

# from selenium import webdriver
# from selenium.webdriver.firefox.service import Service as FirefoxService
# from selenium.webdriver.firefox.options import Options as FirefoxOptions
# from webdriver_manager.firefox import GeckoDriverManager
# from selenium.webdriver.chrome.service import Service as ChromeService
# from selenium.webdriver.chrome.options import Options as ChromeOptions
# from webdriver_manager.chrome import ChromeDriverManager

# class PdfGenerator:
#     """
#     Simple use case:
#         pdf_file = PdfGenerator(['https://google.com']).main()
#         with open('new_pdf.pdf', "wb") as outfile:
#             outfile.write(pdf_file[0].getbuffer())
#     """
#     driver = None
#     # Print options for generating PDF
#     print_options = {
#         'landscape': False,
#         'displayHeaderFooter': False,
#         'printBackground': True,
#         'preferCSSPageSize': True,
#         'paperWidth': 6.97,
#         'paperHeight': 16.5,
#     }

#     def __init__(self, urls: List[str]):
#         self.urls = urls

#     def _get_pdf_from_url(self, url, *args, **kwargs):
#         self.driver.get(url)
#         time.sleep(4)  # allow the page to load, increase if needed

#         print_options = self.print_options.copy()
#         result = self._send_devtools(self.driver, "Page.printToPDF", print_options)
#         return base64.b64decode(result['data'])

#     @staticmethod
#     def _send_devtools(driver, cmd, params):
#         resource = f"/session/{driver.session_id}/chromium/send_command_and_get_result"
#         url = driver.command_executor._url + resource
#         body = json.dumps({'cmd': cmd, 'params': params})
#         response = driver.command_executor._request('POST', url, body)
#         return response.get('value')

#     def _generate_pdfs(self):
#         pdf_files = []
#         for url in self.urls:
#             result = self._get_pdf_from_url(url)
#             file = BytesIO()
#             file.write(result)
#             pdf_files.append(file)
#         return pdf_files

#     def main(self) -> List[BytesIO]:
#         # Detect environment
#         if os.getenv("DOCKER_ENV"):  # Running in Docker, use Firefox
#             webdriver_options = FirefoxOptions()
#             webdriver_options.add_argument('--headless')
            
#             # Correct binary location for Firefox within the Docker container
#             webdriver_options.binary_location = "/usr/bin/firefox"  # Correct the path to Firefox executable
            
#             # Set up driver with Firefox
#             self.driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=webdriver_options)
#         else:  # Running locally, use Chrome
#             webdriver_options = ChromeOptions()
#             webdriver_options.add_argument('--headless')
#             self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=webdriver_options)

#         try:
#             result = self._generate_pdfs()
#         finally:
#             if self.driver:
#                 self.driver.quit()
#         return result


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
        await page.goto(url)
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