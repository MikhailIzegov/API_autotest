import requests
from allure import step

from apis.demoshop.model.demoqa import DemoQA, DemoQAWithSession
from apis.demoshop.utils.get_auth import login, password


def test_add_to_cart_response(login, password):
    add_to_cart_url = "https://demowebshop.tricentis.com/addproducttocart/catalog/31/1/1"
    with step("Авторизуемся"):
        response = requests.post(
            "https://demowebshop.tricentis.com/login",
            data={"Email": login, "Password": password},
            allow_redirects=False
        )
    authorization_cookie = response.cookies.get("NOPCOMMERCE.AUTH")

    with step("Добавляем товар в корзину"):
        result = requests.post(add_to_cart_url, cookies={"NOPCOMMERCE.AUTH": authorization_cookie})

    with step("Проверяем что продукт добавлен"):
        assert result.json()['success'] is True
        assert "The product has been added" in result.json()['message']

        """
    Тут можно написать проверку гибридом, совместив API и UI тесты:
    assert result.json()["updatetopcartsectionhtml"] == f"({cart_items_number})"
    , где cart_items_number - это число товаров в корзине, которое возьмем из UI по локатору
        """


def test_add_to_cart_response_with_model(login, password):
    with step("Авторизуемся"):
        demoqa = DemoQA()
        demoqa.login(email=login, password=password)

    with step("Добавляем товар в корзину"):
        result = demoqa.add_to_cart()

    with step("Проверяем что продукт добавлен"):
        assert result.json()['success'] is True
        assert "The product has been added" in result.json()['message']


def test_add_to_cart_response_with_model_and_session(login, password):
    with step("Авторизуемся"):
        demoqa = DemoQAWithSession()
        demoqa.login(email=login, password=password)

    with step("Добавляем товар в корзину"):
        result = demoqa.add_to_cart()

    with step("Проверяем что продукт добавлен"):
        assert result.json()['success'] is True
        assert "The product has been added" in result.json()['message']
