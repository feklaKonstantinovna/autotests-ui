import pytest
from playwright.sync_api import sync_playwright, expect, Page


@pytest.mark.courses
@pytest.mark.regression
def test_empty_courses_list(chromium_page_with_state: Page):
    chromium_page_with_state.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

    title = chromium_page_with_state.get_by_test_id('courses-list-toolbar-title-text')
    expect(title).to_be_visible()
    expect(title).to_have_text('Courses')

    no_results_block = chromium_page_with_state.get_by_test_id('courses-list-empty-view-title-text')
    expect(no_results_block).to_be_visible()
    expect(no_results_block).to_have_text('There is no results')
