import allure
import pytest
from pages.dashboard.dashboard_page import DashboardPage
from tools.allure.tags import AllureTag

@pytest.mark.dashboard
@pytest.mark.regression

class TestDashboard:
    @allure.tag(AllureTag.REGRESSION, AllureTag.DASHBOARD)
    @allure.title('Check displaying of dashboard page')
    def test_dashboard_displaying(self,dashboard_page_with_state: DashboardPage):
        dashboard_page_with_state.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/dashboard')
        dashboard_page_with_state.sidebar.check_visible()
        dashboard_page_with_state.navbar.check_visible('username')
        dashboard_page_with_state.dashboard_toolbar.check_visible()
