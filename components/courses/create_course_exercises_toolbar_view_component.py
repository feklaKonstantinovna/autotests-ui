from playwright.sync_api import Page, expect
from components.base_component import BaseComponent
from elements.text import Text
from elements.button import Button


class CreateCourseExerciseToolbarViewComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)
        self.title = Text(page, 'create-course-exercises-box-toolbar-title-text', 'Title')
        self.create_exercises_button = Button(page, 'create-course-exercises-box-toolbar-create-exercise-button',
                                              'Exercises button')

    def check_visible(self):

        self.title.check_visible()
        self.title.check_have_text('Exercises')

        self.create_exercises_button.check_visible()

    def click_create_exercise_button(self):
        self.create_exercises_button.click()
