from playwright.sync_api import Page, expect
from components.base_component import BaseComponent
from elements.text import Text
from elements.button import Button


class CreateCourseToolbarViewComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)
        self.title = Text(page, 'create-course-toolbar-title-text', 'Title')
        self.button = Button(page, 'create-course-toolbar-create-course-button', 'Button')

    def check_visible(self, is_create_course_disabled: bool = True):
        # Проверка заголовка
        self.title.check_visible()
        self.title.check_have_text('Create course')

        # Проверка кнопки
        self.button.check_visible()

        if is_create_course_disabled:
            self.button.check_disabled()

        if not is_create_course_disabled:
            self.button.check_enabled()

    def click_create_course_button(self):
        self.button.check_enabled()
        self.button.click()
