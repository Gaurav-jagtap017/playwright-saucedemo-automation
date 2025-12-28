from playwright.sync_api import sync_playwright
from pytest_playwright.pytest_playwright import browser


class BrowserFactory:
    @staticmethod
    def launch():
        playwright = sync_playwright().start()
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        return page, browser, playwright