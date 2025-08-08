import allure
from tools.allure.tags import AllureTag
import pytest
from playwright.sync_api import Page

from fixtures.pages import courses_page_list
from pages.courses.courses_list_page import CoursesListPage

from fixtures.pages import create_course_page
from pages.courses.create_course_page import CreateCoursePage


@pytest.mark.courses
@pytest.mark.regression
@allure.tag(AllureTag.REGRESSION, AllureTag.COURSES )
class TestCourses:
    @allure.title('Check displaying of empty courses list')
    def test_empty_courses_list(self, chromium_page_with_state: Page, courses_page_list: CoursesListPage):
        courses_page_list.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses')
        courses_page_list.navbar.check_visible('username')
        courses_page_list.sidebar.check_visible()
        courses_page_list.toolbar_view.check_visible()

        courses_page_list.check_visible_empty_view()

    @allure.title('Crate course')
    def test_create_course(self, create_course_page: CreateCoursePage, courses_page_list: CoursesListPage):
        # 1. Переход на страницу создания курса
        create_course_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create')
        # 2. Проверка, что тулбар создания курса виден и кнопка создания отключена (так как форма пустая)
        create_course_page.create_course_toolbar.check_visible(is_create_course_disabled=True)
        # 3. Проверка виджета загрузки изображения (ожидаем, что изображение не загружено)
        create_course_page.image_upload_widget.check_visible(is_image_uploaded=False)
        # 4. Проверка формы создания курса - ожидаем пустые поля и значения по умолчанию
        create_course_page.create_course_form.check_visible(
            title="",
            estimated_time="",
            description="",
            max_score="0",
            min_score="0"
        )
        # 5. Проверка видимости тулбара упражнений курса
        create_course_page.create_course_exercise_toolbar.check_visible()

        # 6. Проверка, что отображается пустой вид упражнений (так как их еще нет)
        create_course_page.check_visible_exercises_empty_view()
        # 7. Клик по кнопке создания упражнения (переход к добавлению упражнения)
        create_course_page.create_course_exercise_toolbar.click_create_exercise_button()

        # 8. Загрузка превью-изображения для курса
        image_path = './testdata/files/image.png'
        create_course_page.image_upload_widget.upload_preview_image(file=image_path)

        # 9. Проверка, что изображение успешно загрузилось
        create_course_page.image_upload_widget.check_visible(is_image_uploaded=True)

        # 10. Заполнение формы создания курса тестовыми данными
        create_course_page.create_course_form.fill(
            title="Playwright",
            estimated_time="2 weeks",
            description="Playwright",
            max_score="100",
            min_score="10"
        )

        # 11. Проверка, что кнопка создания курса теперь активна (так как форма заполнена)
        create_course_page.create_course_toolbar.check_visible(is_create_course_disabled=False)
        # 12. Клик по кнопке создания курса (сохранение курса)
        create_course_page.create_course_toolbar.click_create_course_button()
        # 13. Проверка, что тулбар списка курсов отображается
        courses_page_list.toolbar_view.check_visible()
        # 14. Проверка, что созданный курс отображается в списке с корректными данными
        courses_page_list.course_view.check_visible(
            index=0,
            title="Playwright",
            estimated_time="2 weeks",
            max_score="100",
            min_score="10"
        )

    def test_edit_course(self, create_course_page: CreateCoursePage, courses_page_list: CoursesListPage, ):
        # 1. Переход на страницу создания курса
        create_course_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create')

        # 2. Создание курса
        create_course_page.create_course_exercise_toolbar.click_create_exercise_button()
        image_path = './testdata/files/image.png'
        create_course_page.image_upload_widget.upload_preview_image(file=image_path)
        create_course_page.create_course_form.fill(
            title="Playwright",
            estimated_time="2 weeks",
            description="Playwright",
            max_score="100",
            min_score="10"
        )
        create_course_page.create_course_toolbar.click_create_course_button()

        # 3. Проверка созданного курса
        courses_page_list.course_view.check_visible(
            index=0,
            title="Playwright",
            estimated_time="2 weeks",
            max_score="100",
            min_score="10"
        )

        # 4. Редактирование курса
        courses_page_list.course_view.menu.click_edit(0)
        create_course_page.create_course_form.fill(
            title="Playwright Updated",
            estimated_time="3 weeks",
            description="Updated course on Playwright",
            max_score="200",
            min_score="20"
        )
        create_course_page.create_course_toolbar.click_create_course_button()

        # 5. Проверка обновленного курса
        courses_page_list.course_view.check_visible(
            index=0,
            title="Playwright Updated",
            estimated_time="3 weeks",
            max_score="200",
            min_score="20"
        )
