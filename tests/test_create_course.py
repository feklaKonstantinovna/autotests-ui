import pytest
from playwright.sync_api import sync_playwright, expect, Page

from fixtures.pages import courses_page_list
from pages.courses_page_list import CoursesListPage

from fixtures.pages import create_course_page
from pages.create_course_page import CreateCoursePage



@pytest.mark.courses
@pytest.mark.regression
def test_create_course(create_course_page: CreateCoursePage, courses_page_list: CoursesListPage):
    create_course_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create')
    create_course_page.check_visible_create_course_title()
    create_course_page.check_disabled_create_course_button()
    create_course_page.check_visible_image_preview_empty_view()
    create_course_page.check_visible_image_upload_view()
    create_course_page.check_visible_create_course_form(
        title="",
        estimated_time="",
        description="",
        max_score="0",
        min_score="0"
    )
    create_course_page.check_visible_exercises_title()
    create_course_page.check_visible_create_exercise_button()
    create_course_page.check_visible_exercises_empty_view()

    image_path = './testdata/files/image.png'
    create_course_page.upload_preview_image(file=image_path)

    create_course_page.check_visible_image_upload_view()
    create_course_page.fill_create_course_form(
        title="Playwright",
        estimated_time="2 weeks",
        description="Playwright",
        max_score="100",
        min_score="10"
    )
    create_course_page.click_create_course_button()
    courses_page_list.check_visible_courses_title()
    courses_page_list.check_visible_create_course_button()
    courses_page_list.check_visible_course_card(
        index = 0,
        title="Playwright",
        estimated_time="2 weeks",
        max_score="100",
        min_score="10"
    )


