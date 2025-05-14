import pytest
from playwright.sync_api import sync_playwright, Page


from fixtures.pages import courses_page_list
from pages.courses_list_page import CoursesListPage

from fixtures.pages import create_course_page
from pages.create_course_page import CreateCoursePage


@pytest.mark.courses
@pytest.mark.regression
def test_create_course(create_course_page: CreateCoursePage, courses_page_list: CoursesListPage):
    create_course_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create')
    create_course_page.create_course_toolbar.check_visible(is_create_course_disabled=True)
    create_course_page.image_upload_widget.check_visible(is_image_uploaded=False)
    create_course_page.create_course_form.check_visible(
        title="",
        estimated_time="",
        description="",
        max_score="0",
        min_score="0"
    )
    create_course_page.create_course_exercise_toolbar.check_visible()
    create_course_page.check_visible_exercises_empty_view()
    create_course_page.create_course_exercise_toolbar.click_create_exercise_button()


    image_path = './testdata/files/image.png'
    create_course_page.image_upload_widget.upload_preview_image(file=image_path)

    create_course_page.image_upload_widget.check_visible(is_image_uploaded=True)
    create_course_page.create_course_form.fill(
        title="Playwright",
        estimated_time="2 weeks",
        description="Playwright",
        max_score="100",
        min_score="10"
    )
    create_course_page.create_course_toolbar.check_visible(is_create_course_disabled=False)
    create_course_page.create_course_toolbar.click_create_course_button()
    courses_page_list.toolbar_view.check_visible()
    courses_page_list.course_view.check_visible(
        index=0,
        title="Playwright",
        estimated_time="2 weeks",
        max_score="100",
        min_score="10"
    )
