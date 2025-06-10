from playwright.sync_api import Page, expect

from components.authentication.registration_form_component import RegistrationFormComponent
from elements.button import Button
from pages.base_page import BasePage
from elements.link import Link
import re


class RegistrationPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)



        self.registration_form = RegistrationFormComponent(page)
        self.login_link = Link(page, 'registration-page-login-link', 'Login')
        self.registration_button = Button(page,'registration-page-registration-button', 'Registration')

    def click_login_link(self):
        self.login_link.click()
        self.check_current_url(re.compile('.*/auth/login'))

    def click_registration_button(self):
        self.registration_button.click()



