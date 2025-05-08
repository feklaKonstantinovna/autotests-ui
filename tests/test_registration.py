from playwright.sync_api import sync_playwright, Page, expect
import pytest

from fixtures.pages import registration_page
from pages.registration_page import RegistrationPage

from fixtures.pages import dashboard_page
from pages.dashboard_page import DashboardPage

user_data = {
    ("user.name@gmail.com ", "user", "password")
}

user_ids = {
    "successful user registration"
}


@pytest.mark.regression
@pytest.mark.registration
@pytest.mark.parametrize('email, username, password', user_data, ids=user_ids)
def test_successful_registration(email: str, username: str, password: str, registration_page: RegistrationPage,
                                 dashboard_page: DashboardPage):
    registration_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')
    registration_page.fill_registration_form(email=email, username=username, password=password)
    registration_page.click_registration_button()
    dashboard_page.check_dashboard_title()
