from playwright.sync_api import sync_playwright, expect


with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

    email_input = page.get_by_test_id('registration-form-email-input').locator('input')
    email_input.fill('user.name@gmail.com')

    username_input = page.get_by_test_id('registration-form-username-input').locator('input')
    username_input.fill('username')

    password_input = page.get_by_test_id('registration-form-password-input').locator('input')
    password_input.fill('password')

    registration_button = page.get_by_test_id('registration-page-registration-button')
    registration_button.click()

    context.storage_state(path="browser-state.json")

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(storage_state="browser-state.json")
    page = context.new_page()

    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

    courses_display = page.get_by_test_id('courses-list-toolbar-title-text')
    expect(courses_display).to_have_text('Courses')

    text_results_display = page.get_by_test_id('courses-list-empty-view-title-text')
    expect(text_results_display).to_have_text('There is no results')

    icon_display = page.get_by_test_id('courses-list-empty-view-icon')
    expect(icon_display).to_be_visible()

    description_display = page.get_by_test_id('courses-list-empty-view-description-text')
    expect(description_display).to_have_text('Results from the load test pipeline will be displayed here')


