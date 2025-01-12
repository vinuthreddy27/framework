import time
from selenium.webdriver.support.expected_conditions import presence_of_element_located, visibility_of_element_located
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:


    def __init__(self,driver):
        self.driver=driver
        self.wait=WebDriverWait(self.driver,7,poll_frequency=2.5)


    def generate_random_email(self):
        timestamp = time.ctime().split()[3]
        timestamp1 = timestamp.replace(":", "")
        return "vinuth" + timestamp1 + "@gmail.com"


    def click_on_element(self,locator):
        element=self.wait.until(presence_of_element_located(locator))
        element.click()

    def send_keys_on_element(self,locator,value):
        element=self.wait.until(presence_of_element_located(locator))
        element.clear()
        element.send_keys(value)

    def submit_the_form(self,locator):
        element=self.wait.until(presence_of_element_located(locator))
        element.submit()

    def display_status(self,locator):
        element=self.wait.until(visibility_of_element_located(locator))
        return element.is_displayed()

    def get_text(self,locator):
        element=self.wait.until(visibility_of_element_located(locator))
        print(element.text)

    def verify_radiobtn(self,locator):
        element = self.wait.until(visibility_of_element_located(locator))
        return element.is_selected()

