import pytest
from playwright.sync_api import Page

from fixtures.pages import courses_page_list
from pages.courses.courses_list_page import CoursesListPage


@pytest.mark.courses
@pytest.mark.regression
def test_empty_courses_list(chromium_page_with_state: Page, courses_page_list: CoursesListPage):
    courses_page_list.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses')
    courses_page_list.navbar.check_visible('username')
    courses_page_list.sidebar.check_visible()
    courses_page_list.toolbar_view.check_visible()
    
    courses_page_list.check_visible_empty_view()
