


from project1.library.basepage import BasePage


class Enquiry_page(BasePage):
    text_area_locator=("name","enquiry")
    name=("name","name")
    email=("name","email")
    submit_btn=("xpath","//input[@value='Submit']")
    continue_btn3=("xpath","//a[.='Continue']")


    def enquiry(self,name,mail,text):
        self.send_keys_on_element(self.name, name)
        self.send_keys_on_element(self.email,mail)
        self.send_keys_on_element(self.text_area_locator,text)
        self.click_on_element(self.submit_btn)
        self.click_on_element(self.continue_btn3)