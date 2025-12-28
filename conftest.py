import os
import pytest
import pytest_html

from core.browser_factory import BrowserFactory
from datetime import datetime

@pytest.fixture
def page(request):
    page, browser, playwright = BrowserFactory.launch()
    yield page

    if request.node.rep_call.failed:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        os.makedirs("reports/screenshots", exist_ok=True)
        screenshot_path = f"reports/screenshots/{request.node.name}_{timestamp}.png"
        page.screenshot(path=screenshot_path, full_page=True)

    browser.close()
    playwright.stop()
