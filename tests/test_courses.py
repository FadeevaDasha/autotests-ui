from playwright.sync_api import expect, Page
import pytest

@pytest.mark.regression
@pytest.mark.courses
def test_empty_courses_list(chromium_page_with_state: Page):

        courses_title = chromium_page_with_state.get_by_test_id('courses-list-toolbar-title-text')
        expect(courses_title).to_be_visible()
        expect(courses_title).to_have_text("Courses")

        title_empty_list = chromium_page_with_state.get_by_test_id('courses-list-empty-view-title-text')
        expect(title_empty_list).to_be_visible()
        expect(title_empty_list).to_have_text("There is no results")

        icon_empty_list = chromium_page_with_state.get_by_test_id('courses-list-empty-view-icon')
        expect(icon_empty_list).to_be_visible()

        description_empty_list = chromium_page_with_state.get_by_test_id('courses-list-empty-view-description-text')
        expect(description_empty_list).to_be_visible()
        expect(description_empty_list).to_have_text("Results from the load test pipeline will be displayed here")