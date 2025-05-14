from components.base_component import BaseComponent
from playwright.sync_api import Page, expect


class CourseViewMenuComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        # Описание кнопки изменения/удаления готовой карточки курса
        self.menu_button = page.get_by_test_id('course-view-menu-button')
        # Описание кнопки изменения готовой карточки курса
        self.edit_menu_button = page.get_by_test_id('course-view-edit-menu-item')
        # Описание кнопки удаления готовой карточки курса
        self.delete_menu_button = page.get_by_test_id('course-view-delete-menu-item')

    def click_edit(self, index: int):
        self.menu_button.nth(index).click()

        expect(self.edit_menu_button.nth(index)).to_be_visible()
        self.edit_menu_button.nth(index).click()

    def click_delete_course(self, index: int):
        self.menu_button.nth(index).click()

        expect(self.delete_menu_button.nth(index)).to_be_visible()
        self.delete_menu_button.nth(index).click()