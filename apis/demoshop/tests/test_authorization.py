import requests
from selene import browser, have
from allure import step
from apis.demoshop.utils.get_auth import login, password


WEB_URL = 'http://demowebshop.tricentis.com'
API_URL = 'http://demowebshop.tricentis.com'  # Зачастую может отличаться от WEB_URL


def test_login_through_ui(login, password):
    with step('Open login page'):
        browser.open("http://demowebshop.tricentis.com/login")

    with step("Fill login form"):
        browser.element("#Email").send_keys(login)
        browser.element("#Password").send_keys(password).press_enter()

    with step("Verify successful authorization"):
        browser.element(".account").should(have.text(login))


def test_login_through_api_without_fixture(login, password):
    with step("Get auth cookie through API"):
        auth_cookie_name = 'NOPCOMMERCE.AUTH'
        url = API_URL + '/login'
        payload = {
            'Email': login,
            'Password': password,
            'RememberMe': False
        }
        response = requests.request('POST', url, data=payload, allow_redirects=False)
        cookie = response.cookies.get(auth_cookie_name)

    with step("Open browser with auth cookie"):
        browser.open(WEB_URL)  # Особенность Selenium, что
    # без инициализации браузера куку не установит!

        browser.driver.add_cookie({"name": auth_cookie_name, "value": cookie})  # Код по получению куки можно вынести
        # в фикстуру и вместо переменной "cookie" можно передать фикстуру из get_auth.py

        browser.open(WEB_URL)  # Особенность Selenium, что
    # еще надо открыть его заново!

    with step("Verify successful authorization"):
        browser.element(".account").should(have.text(login))
