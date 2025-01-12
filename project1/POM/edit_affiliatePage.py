

from project1.library.basepage import BasePage


class Edit_affiliate(BasePage):

    company_text_field = ("name", "company")
    website_textfield = ("name", "website")
    tax_textfield = ("name", "tax")
    payment_mode_btn = ("xpath", "//input[@value='paypal']")
    paypal_textfield = ("name", "paypal")
    continue_btn = ("xpath", "//input[@type='submit']")

    def edit_affiliate(self,company_name,website,tax,pay):
        self.send_keys_on_element(self.company_text_field,company_name)
        self.send_keys_on_element(self.website_textfield,website)
        self.send_keys_on_element(self.tax_textfield,tax)
        self.click_on_element(self.payment_mode_btn)
        self.send_keys_on_element(self.paypal_textfield,pay)
        self.click_on_element(self.continue_btn)

    def modify(self):
        self.send_keys_on_element(self.company_text_field,"my company")
        self.click_on_element(self.continue_btn)

