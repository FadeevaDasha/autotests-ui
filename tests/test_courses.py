from playwright.sync_api import sync_playwright, expect, Page
import pytest


@pytest.mark.courses
@pytest.mark.regression
def test_empty_courses_list(chromium_page_with_state: Page):

        chromium_page_with_state.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

        courses_display = chromium_page_with_state.get_by_test_id('courses-list-toolbar-title-text')
        expect(courses_display).to_have_text('Courses')

        text_results_display = chromium_page_with_state.get_by_test_id('courses-list-empty-view-title-text')
        expect(text_results_display).to_have_text('There is no results')

        icon_display = chromium_page_with_state.get_by_test_id('courses-list-empty-view-icon')
        expect(icon_display).to_be_visible()

        description_display = chromium_page_with_state.get_by_test_id('courses-list-empty-view-description-text')
        expect(description_display).to_have_text('Results from the load test pipeline will be displayed here')