

from project1.library.basepage import BasePage


class Modify_account(BasePage):
    telephone_locator = ("name", "telephone")
    continue_btn = ("xpath", "//input[@value='Continue']")


    def modify(self,phno):
     self.send_keys_on_element(self.telephone_locator, phno)
     self.click_on_element(self.continue_btn)

