from project1.POM.dashboard_page import LandingPage
from project1.configurations.config import TestData
from project1.library.basepage import BasePage


class LoginPage(BasePage):
    email_textfield = ("css selector", "#input-email")
    password_textfield = ("css selector", "#input-password")
    login_btn = ("xpath", "//input[@value='Login']")

    def login_into_application(self):
        self.send_keys_on_element(self.email_textfield, TestData.username)
        self.send_keys_on_element(self.password_textfield, TestData.password)
        self.click_on_element(self.login_btn)

        landing_page=LandingPage(self.driver)
        return landing_page

    def login(self,email,password):
        self.send_keys_on_element(self.email_textfield,email)
        self.send_keys_on_element(self.password_textfield,password)
        self.click_on_element(self.login_btn)

        landing_page=LandingPage(self.driver)
        return landing_page