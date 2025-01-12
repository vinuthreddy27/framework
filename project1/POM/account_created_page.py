
from project1.library.basepage import BasePage


class Registered_success(BasePage):

    message=("xpath","//div[@id='content']/.//p[.='Congratulations! Your new account has been successfully created!']")

    def success_msg(self):
        self.get_text(self.message)
        self.display_status(self.message)

