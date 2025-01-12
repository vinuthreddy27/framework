

from project1.library.basepage import BasePage


class wishlist_page(BasePage):
    remove_btn=("xpath","//a[@class='btn btn-danger']")
    message=("xpath","//div[@class='alert alert-success alert-dismissible']")

    def click_remove_btn(self):
        self.click_on_element(self.remove_btn)

    def proper_message(self):
        self.get_text(self.message)
        self.display_status(self.message)