

from project1.library.basepage import BasePage


class Subscription_page(BasePage):
    yes=("xpath","//input[@value='1']")
    no=("xpath","//input[@value='0']")


    def Yes(self):
        self.click_on_element(self.yes)

    def No(self):
        self.click_on_element(self.no)

    def validate_yes(self):
         return self.verify_radiobtn(self.yes)

    def validate(self):
         return self.verify_radiobtn(self.no)