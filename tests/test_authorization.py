from playwright.sync_api import sync_playwright, expect, Page
import pytest

from fixtures.browsers import chromium_page
from fixtures.pages import login_page

from pages.login_page import LoginPage

user_data = {
    ("user.name@gmail.com ", "password"),
    ("user.name@gmail.com", "  "),
    ("  ", "password"),
}

user_ids = {
    "invalid_email_and_password",
    "invalid_email_and_empty_password",
    "empty_email_and_invalid_password"
}


@pytest.mark.regression
@pytest.mark.authorization
@pytest.mark.parametrize('email, password', user_data, ids=user_ids)
def test_wrong_email_or_password_authorization(email: str, password: str, login_page: LoginPage):
    login_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login')
    login_page.login_form.fill(email=email, password=password)
    login_page.login_form.check_visible(email=email, password=password)
    login_page.click_login_button()
    login_page.check_visible_wrong_email_or_password_alert()
