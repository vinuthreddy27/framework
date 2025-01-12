from project1.POM.changepassword_page import PasswordChangePage
from project1.library.basepage import BasePage


class LandingPage(BasePage):
    change_password_locator = ("xpath", "//ul[@class='list-unstyled']/..//a[.='Change your password']")

    edit_account_link=("xpath","//*[normalize-space()='Edit your account information']")
    success_pass_changed = ("xpath", "//*[.='Success: Your password has been successfully updated.']")

    def proper_message(self):
        return self.display_status(self.edit_account_link)

    def success_message(self):
        self.get_text(self.success_pass_changed)
        return self.display_status(self.success_pass_changed)

    def click_on_password_link(self):
        self.click_on_element(self.change_password_locator)

        password_page = PasswordChangePage(self.driver)
        return password_page