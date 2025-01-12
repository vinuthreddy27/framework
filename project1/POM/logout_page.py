from project1.library.basepage import BasePage


class Logout_page(BasePage):
    message=("xpath","//p[.='You have been logged off your account. It is now safe to leave the computer.']")


    def dispaly_success_logout(self):
        self.get_text(self.message)
        self.display_status(self.message)