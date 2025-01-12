from project1.library.basepage import BasePage


class Review_page(BasePage):
    yourname_tf = ("id", "input-name")
    text_area = ("name", "text")
    rating_rb = ("xpath", "//input[@value='5']")
    continue_btn = ("id", "button-review")
    warning_msgg=("xpath","//div[contains(@class,'alert')]")
    success_msg=("xpath","//*[.=' Thank you for your review. It has been submitted to the webmaster for approval.']")

    def add_a_review(self,yourname,text):
        self.send_keys_on_element(self.yourname_tf,yourname)
        self.send_keys_on_element(self.text_area,text)
        self.click_on_element(self.rating_rb)
        self.click_on_element(self.continue_btn)

    def display_success_msg(self):
        self.get_text(self.success_msg)
        self.display_status(self.warning_msgg)

    def display_error_msg(self):
        self.get_text(self.warning_msgg)
        self.display_status(self.warning_msgg)
