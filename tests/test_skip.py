import pytest
from selene.support.shared import browser
from selene.support.shared.jquery_style import s


@pytest.mark.parametrize(['browser_height', 'browser_width'],
                         [(900, 600), (1980, 1024)],
                         ids=['Desktop', 'Mob'])
def test_skip_mob_version(browser_height, browser_width):
    browser.config.window_height = browser_height
    browser.config.window_width = browser_width
    if browser_height == 900 and browser_width == 600:
        pytest.skip('Тест для мобильной версии')
    else:
        browser.open('/')
        s('.HeaderMenu-link--sign-in').click()


@pytest.mark.parametrize(['browser_height', 'browser_width'],
                         [(900, 600), (1980, 1024)],
                         ids=['Desktop', 'Mob'])
def test_skip_desktop_version(browser_height, browser_width):
    browser.config.window_height = browser_height
    browser.config.window_width = browser_width
    if browser_height == 1980 and browser_width == 1024:
        pytest.skip('Тест для десктопной версии')
    else:
        browser.open('/')
        s('.Button-label').click()
        s('.HeaderMenu-link--sign-in').click()