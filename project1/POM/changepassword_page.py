from project1.library.basepage import BasePage


class PasswordChangePage(BasePage):
    password = ("name", "password")
    c_password = ("name", "confirm")
    conform_btn = ("xpath", "//input[@value='Continue']")
    password_error_msg = ("xpath", "//div[.='Password must be between 4 and 20 characters!']")
    error_msg=("xpath","//div[.='Password confirmation does not match password!']")

    def change(self):
       self.send_keys_on_element(self.password,"selenium")
       self.send_keys_on_element(self.c_password,"selenium")
       self.click_on_element(self.conform_btn)

    def display_error_msg(self):
       pass

    def display_error_msg2(self):
       pass