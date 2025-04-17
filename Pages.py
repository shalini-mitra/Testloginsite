from selenium.webdriver.common.by import By
#Defining the page class, locators and methods in the class

class LoginPage :
       USERNAME_LOCATOR = (By.ID, 'username')
       PASSWORD_LOCATOR = (By.ID, 'password')
       SUBMIT_LOCATOR = (By.ID, 'submit')
       SUCCESSFUL_TEXT_LOCATOR = (By.XPATH, '//strong[contains(text(), "Congratulations")]')
       LOGOUT_BUTTON_LOCATOR = (By.XPATH, '//a[contains(@href, "https://practicetestautomation.com/practice-test-login/")]')

       def __init__(self, driver):
           self.driver = driver

       def enter_username(self, username_text):
           self.driver.find_element(*self.USERNAME_LOCATOR).send_keys(username_text)

       def enter_password(self, password_text):
           self.driver.find_element(*self.PASSWORD_LOCATOR).send_keys(password_text)

       def click_submit_button(self):
           self.driver.find_element(*self.SUBMIT_LOCATOR).click()

       def get_successful_text(self):
           return self.driver.find_element(*self.SUCCESSFUL_TEXT_LOCATOR).text

       def get_logout_text(self):
           return self.driver.find_element(*self.LOGOUT_BUTTON_LOCATOR).text

       def enter_into_the_field(self, username_text, password_text):
           self.enter_username(username_text)
           self.enter_password(password_text)

       def click_logout_button(self):
           self.driver.find_element(*self.LOGOUT_BUTTON_LOCATOR).click()








