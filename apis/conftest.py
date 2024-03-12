import os
import pytest
from selene import browser
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from apis.general_utils import attach


@pytest.fixture(scope='module', autouse=True)
def load_env():
    load_dotenv()


@pytest.fixture(scope="function", autouse=True)
def setup_browser():
    options = Options()
    selenoid_capabilities = {
        'browserName': 'chrome',
        'browserVersion': '100.0',
        'selenoid:options': {
            'enableVNC': True,
            'enableVideo': True
        }
    }
    options.capabilities.update(selenoid_capabilities)

    selenoid_login = os.getenv('SELENOID_LOGIN')
    selenoid_password = os.getenv('SELENOID_PASSWORD')

    driver = webdriver.Remote(
        command_executor=f'https://{selenoid_login}:{selenoid_password}@selenoid.autotests.cloud/wd/hub',
        options=options
    )

    browser.config.driver = driver

    yield

    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_html(browser)
    attach.add_video(browser)

    browser.quit()