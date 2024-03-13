import requests

from requests import sessions


class DemoQA:
    def __init__(self):
        self.base_url = "https://demowebshop.tricentis.com"
        self.authorization_cookie = None

    def login(self, email, password):
        response = requests.post(
            url=f"{self.base_url}/login",
            data={"Email": email, "Password": password},
            allow_redirects=False
        )
        self.authorization_cookie = response.cookies.get("NOPCOMMERCE.AUTH")

    def add_to_cart(self, product="31/1/1", count=2):
        response = None
        for i in range(count):
            response = requests.post(
                url=f"{self.base_url}/addproducttocart/catalog/{product}",
                cookies={"NOPCOMMERCE.AUTH": self.authorization_cookie}
            )
        return response


class DemoQAWithSession:
    def __init__(self):
        self.base_url = "https://demowebshop.tricentis.com"

    def demoshop_api(self, method, url, **kwargs):
        with sessions.Session() as session:
            response = session.request(method=method, url=self.base_url + url, **kwargs)
        return response

    def login(self, email, password):
        self.demoshop_api(
            'post',
            url="/login",
            data={"Email": email, "Password": password},
            allow_redirects=False
        )

    def add_to_cart(self, product_id="31/1/1", count=2):
        response = None
        for i in range(count):
            response = self.demoshop_api(
                'post',
                url=f"/addproducttocart/catalog/{product_id}"
            )
        return response
