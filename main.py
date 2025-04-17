from selenium import webdriver
from Pages import LoginPage
import requests
import data
import time

class TestLoginPage:
    @classmethod
    def setup_class(cls):
        from selenium.webdriver import DesiredCapabilities
        capabilities = DesiredCapabilities.CHROME
        capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}
        cls.driver = webdriver.Chrome()

    @staticmethod
    def is_url_reachable(url):
        try:
            response = requests.get(url,timeout=10)
            return response.status_code == 200
        except requests.exceptions.RequestException:
            return False


    if is_url_reachable(data.LOGIN_PAGE_URL):
        print("Connected to TestLogin site")
    else:
        print("Cannot connect to the server")

    def test_login_with_credentials(self):
        self.driver.get(data.LOGIN_PAGE_URL)
        test_login = LoginPage(self.driver)
        test_login.enter_into_the_field(data.USERNAME, data.PASSWORD)
        time.sleep(2)
        test_login.click_submit_button()

        #Check the current URL immediately after the login attempt
        current_url = self.driver.current_url
        assert data.LOGOUT_PAGE_URL in current_url, f'URL validation failed. Current_URL: {current_url}'
        text_appears = test_login.get_successful_text()
        assert data.TEXT_APPEARS in text_appears, f'Expected to appear {data.TEXT_APPEARS}, but appears {text_appears}'
        button_text = test_login.get_logout_text()
        assert button_text in data.LOGOUT_BUTTON_TEXT, f'Expected {data.LOGOUT_BUTTON_TEXT}, but got {button_text}'
        time.sleep(2)
        test_login.click_logout_button()
    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
