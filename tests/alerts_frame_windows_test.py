import time
from pages.alerts_frame_windows_page import BrowserWindowsPage, AlertsPage, FramePage, NestedFramesPage
from conftest import driver


class TestBrowserWindows:

    def test_new_tab(self, driver):
        browser_window_page = BrowserWindowsPage(driver, "https://demoqa.com/browser-windows")
        browser_window_page.open()
        text_result = browser_window_page.check_opened_new_tab()
        assert text_result == 'This is a sample page', "the new tab has not opened or incorrect tab has opened"

    def test_new_window(self, driver):
        browser_window_page = BrowserWindowsPage(driver, "https://demoqa.com/browser-windows")
        browser_window_page.open()
        text_result = browser_window_page.check_opened_new_tab()
        assert text_result == 'This is a sample page', "the new window has not opened or incorrect tab has opened"


class TestAlertPage:

    def test_see_alert(self, driver):
        alert_page = AlertsPage(driver, 'https://demoqa.com/alerts')
        alert_page.open()
        alert_text = alert_page.check_see_alert()
        assert alert_text == 'You clicked a button', "Alert did not  show up"

    def test_alert_appear_5_sec(self, driver):
        alert_page = AlertsPage(driver, 'https://demoqa.com/alerts')
        alert_page.open()
        alert_text = alert_page.check_alert_appear_5_sec()
        assert alert_text == 'This alert appeared after 5 seconds', "Alert did not show up"

    def test_confirm_alert(self, driver):
        alert_page = AlertsPage(driver, 'https://demoqa.com/alerts')
        alert_page.open()
        alert_text = alert_page.check_confirm_alert()
        assert alert_text == 'You selected Ok', "Alert did not show up"

    def test_prompt_alert(self, driver):
        alert_page = AlertsPage(driver, 'https://demoqa.com/alerts')
        alert_page.open()
        text, alert_text = alert_page.check_prompt_alert()
        assert text in alert_text, "Alert did not show up"


class TestFramePage:

    def testFramesPage(self, driver):
        frame_page = FramePage(driver, 'https://demoqa.com/frames')
        frame_page.open()
        result_frame1 = frame_page.check_frame('frame1')
        result_frame2 = frame_page.check_frame('frame2')
        assert result_frame1 == ['This is a sample page', '500px', '350px'], 'The frame does not exist'
        assert result_frame2 == ['This is a sample page', '100px', '100px'], 'The frame does not exist'


class TestNestedFramesPage:

    def test_nested_frames(self, driver):
        nested_frame_page = NestedFramesPage(driver, 'https://demoqa.com/nestedframes')
        nested_frame_page.open()
        parent_text, child_text = nested_frame_page.check_nested_frame()
        assert parent_text == "Parent frame", 'Nested frame does not exist'
        assert child_text == "Child Iframe", 'Nested frame does not exist'
