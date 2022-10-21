import pytest
from selene.support.shared import browser
from selene.support.shared.jquery_style import s

browser.config.hold_browser_open = True


@pytest.fixture(scope='function')
def desktop_fixture():
    browser.config.window_height = 1024
    browser.config.window_width = 1980


@pytest.fixture(scope='function')
def mobile_fixture():
    browser.config.window_height = 600
    browser.config.window_width = 900


def test_github_desktop(desktop_fixture):
    browser.open('/')
    s('.HeaderMenu-link--sign-in').click()


def test_github_mob(mobile_fixture):
    browser.open('/')
    s('.Button-label').click()
    s('.HeaderMenu-link--sign-in').click()
