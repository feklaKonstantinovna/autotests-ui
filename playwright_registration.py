from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')

    email_input_registration = page.get_by_test_id('registration-form-email-input').locator('input')
    email_input_registration.fill('user.name@gmail.com')

    username_input_registration = page.get_by_test_id('registration-form-username-input').locator('input')
    username_input_registration.fill('username')

    password_input_registration = page.get_by_test_id('registration-form-password-input').locator('input')
    password_input_registration.fill('password')

    registration_button = page.get_by_test_id('registration-page-registration-button')
    registration_button.click()
    expect(page).to_have_url('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/dashboard')

    title_dashboard = page.get_by_test_id('dashboard-toolbar-title-text')
    expect(title_dashboard).to_be_visible()
    expect(title_dashboard).to_have_text("Dashboard")




    page.wait_for_timeout(5000)
