import pytest
from selene.support.shared import browser
from selene.support.shared.jquery_style import s


@pytest.mark.parametrize(['browser_height', 'browser_width'],
                         [(600, 900), (1024, 1980)],
                         ids=['Mob', 'Desktop'])
def test_skip_mob_version(browser_height, browser_width):
    browser.config.window_height = browser_height
    browser.config.window_width = browser_width
    if browser_height == 600 and browser_width == 900:
        pytest.skip('Тест для мобильной версии')

    browser.open('/')
    s('.HeaderMenu-link--sign-in').click()


@pytest.mark.parametrize(['browser_height', 'browser_width'],
                         [(600, 900), (1024, 1980)],
                         ids=['Mob', 'Desktop'])
def test_skip_desktop_version(browser_height, browser_width):
    browser.config.window_height = browser_height
    browser.config.window_width = browser_width
    if browser_height == 1024 and browser_width == 1980:
        pytest.skip('Тест для десктопной версии')

    browser.open('/')
    s('.Button-label').click()
    s('.HeaderMenu-link--sign-in').click()
