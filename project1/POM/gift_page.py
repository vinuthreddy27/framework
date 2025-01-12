
from project1.library.basepage import BasePage


class Gift_page(BasePage):

    receipient_locator=("id","input-to-name")
    receipient_email=("id","input-to-email")
    your_name=("id","input-from-name")
    your_email=("id","input-from-email")
    birthday_btn=("xpath","//input[@value='7']")
    message=("xpath","//textarea[@id='input-message']")
    amount=("xpath","//input[@name='amount']")
    agree_checkbox=("xpath","//input[@name='agree']")
    continue_btn=("xpath","//input[@value='Continue']")

    proper_message=("xpath","//p[contains(.,'Thank you for purchasing a gift certificate!')]")


    def gift(self,name,mail,msg,amnt):
        self.send_keys_on_element(self.receipient_locator,name)
        self.send_keys_on_element(self.receipient_email,mail)

        self.click_on_element(self.birthday_btn)
        self.send_keys_on_element(self.message,msg)
        self.send_keys_on_element(self.amount,amnt)
        self.click_on_element(self.agree_checkbox)
        self.click_on_element(self.continue_btn)

    def get_message(self):
        self.get_text(self.proper_message)
        self.display_status(self.proper_message)