import pytest
from selene.support.shared import browser
from selene.support.shared.jquery_style import s


@pytest.fixture(scope='function')
def browser_config(request):
    browser.config.window_width = request.param[0]
    browser.config.window_height = request.param[1]


@pytest.mark.parametrize('browser_config', [(900, 600), (1980, 1024)], indirect=True)
def test_with_params(browser_config):
    browser.open('/')
    if browser.config.window_width == 900 and browser.config.window_height == 600:
        s('.Button-label').click()
    s('.HeaderMenu-link--sign-in').click()