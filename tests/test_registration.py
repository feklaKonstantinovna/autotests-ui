from playwright.sync_api import sync_playwright, Page
import pytest

from fixtures.pages import registration_page
from pages.registration_page import RegistrationPage

from fixtures.pages import dashboard_page
from pages.dashboard_page import DashboardPage


@pytest.mark.registration
@pytest.mark.regression
def test_successful_registration(registration_page: RegistrationPage,
                                 dashboard_page: DashboardPage):
    email = "testuser@example.com"
    username = "testuser"
    password = "SecurePassword123"

    registration_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')
    registration_page.registration_form.fill(email=email, username=username, password=password)
    registration_page.registration_form.check_visible(email=email, username=username, password=password)
    registration_page.click_registration_button()
    dashboard_page.dashboard_toolbar.check_visible()
