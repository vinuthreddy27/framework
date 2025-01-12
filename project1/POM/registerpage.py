from project1.POM.account_created_page import Registered_success
from project1.library.basepage import BasePage


class Register_page(BasePage):

    first_name_locator = ("id", "input-firstname")
    last_name_locator = ("id", "input-lastname")
    email_locator = ("id", "input-email")
    telephone_locator = ("id", "input-telephone")
    password_locator = ("id", "input-password")
    conform_password_locator = ("id", "input-confirm")
    radio_btn = ("xpath", "//label[@class='radio-inline']/input[@value = '1']")
    privacy_policy_check_box_btn = ("xpath", "//input[@type='checkbox']")
    register_btn = ("xpath", "//input[@value='Continue']")

    def register(self,fn,ln,pno,password,c_password):
        self.send_keys_on_element(self.first_name_locator,fn)
        self.send_keys_on_element(self.last_name_locator,ln)
        self.send_keys_on_element(self.email_locator,self.generate_random_email())
        self.send_keys_on_element(self.telephone_locator,pno)
        self.send_keys_on_element(self.password_locator,password)
        self.send_keys_on_element(self.conform_password_locator,c_password)
        self.click_on_element(self.radio_btn)
        self.click_on_element(self.privacy_policy_check_box_btn)


    def submit_(self):
        self.submit_the_form(self.password_locator)

        account_creationPage=Registered_success(self.driver)
        return account_creationPage
