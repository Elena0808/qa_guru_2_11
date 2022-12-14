import os
from selene.support.shared import browser
import pytest


@pytest.fixture(scope='function', autouse=True)
def setup_browser():
    browser.config.base_url = 'https://github.com'
    browser.config.browser_name = os.getenv('selene.browser_name', 'chrome')
    browser.config.timeout = float(os.getenv('selene.timeout', '3'))
    browser.config.hold_browser_open = False
