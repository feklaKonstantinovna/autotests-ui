import pytest
import allure
from fixtures.pages import login_page

from pages.authentication.login_page import LoginPage
from pages.authentication.registration_page import RegistrationPage
from pages.dashboard.dashboard_page import DashboardPage


@pytest.mark.regression
@pytest.mark.authorization
@allure.tag("REGRESSION", "AUTHORIZATION" )
class TestAuthorization:
    @allure.title('User login with correct email and password')
    @allure.tag('USER_LOGIN')
    def test_successful_authorization(self,
                                      dashboard_page: DashboardPage,
                                      registration_page: RegistrationPage,
                                      login_page: LoginPage):
        registration_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')
        registration_page.registration_form.fill(email="testuser@example.com", username="testuser",
                                                 password="SecurePassword123")
        registration_page.click_registration_button()

        dashboard_page.dashboard_toolbar.check_visible()
        dashboard_page.navbar.check_visible('testuser')
        dashboard_page.sidebar.check_visible()
        dashboard_page.sidebar.click_logout()

        login_page.login_form.fill(email="testuser@example.com", password="SecurePassword123")
        login_page.login_button.click()

    @pytest.mark.parametrize('email, password',
                             [("user.name@gmail.com ", "password"),
                              ("user.name@gmail.com", "  "),
                              ("  ", "password"), ])

    @allure.title('User login with wrong email or password')
    @allure.tag('USER_LOGIN')
    def test_wrong_email_or_password_authorization(self, email: str, password: str, login_page: LoginPage):

        login_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login')
        login_page.login_form.fill(email=email, password=password)
        login_page.login_form.check_visible(email=email, password=password)
        login_page.click_login_button()
        login_page.check_visible_wrong_email_or_password_alert()

    @allure.title('Navigation from login page to registration page')
    @allure.tag('NAVIGATION')
    def test_navigate_from_authorization_to_registration(self,
                                                         login_page: LoginPage,
                                                         registration_page: RegistrationPage):
        login_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login')
        login_page.click_registration_link()

        registration_page.registration_form.check_visible(email="", username="",
                                                 password="")

