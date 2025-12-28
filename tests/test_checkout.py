import os
from pages.login_page import LoginPage
from business.checkout_flow import CheckoutFlow
from utils.user_factory import UserFactory

def test_user_can_checkout_successfully(page):
    username = os.getenv('TEST_USERNAME')
    password = os.getenv('TEST_PASSWORD')
    if not username:
        raise ValueError("Environment variable 'TEST_USERNAME' is not set.")
    if not password:
        raise ValueError("Environment variable 'TEST_PASSWORD' is not set.")
    LoginPage(page).login(username, password)

    flow = CheckoutFlow(page)
    confirmation = flow.complete_checkout(UserFactory.standard_user())

    assert "THANK YOU" in confirmation.upper()