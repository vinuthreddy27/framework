from project1.POM.review_page import Review_page
from project1.POM.wishlist_page import wishlist_page
from project1.library.basepage import BasePage


class ProductPage(BasePage):

    product_link = ("link text", "iPod Touch")
    review_link = ("xpath", "//a[.='Write a review']")
    cart_btn=("xpath","//span[.='Add to Cart']")
    wishlist_btn=("css selector","button[data-original-title='Add to Wish List']")
    message=("xpath","//div[contains(@class,'alert')]")
    no_Product_match=("xpath","//p[.='There is no product that matches the search criteria.']")
    product_match=("xpath","//h2[.='Products meeting the search criteria']")

    def btn(self):
        self.click_on_element(self.cart_btn)

    def message_(self):
        self.display_status(self.message)

    def wishlist_link(self):
        self.click_on_element(self.wishlist_btn)

    def click_product_link(self):
        self.click_on_element(self.product_link)
        self.click_on_element(self.review_link)

        page_review=Review_page(self.driver)
        return page_review

    def _text(self):
        self.get_text(self.message)
        self.display_status(self.message)

        page_wishlist=wishlist_page(self.driver)
        return page_wishlist

    def get_message(self):
        self.get_text(self.product_match)
        self.display_status(self.product_match)

    def no_message(self):
        self.get_text(self.no_Product_match)
        self.display_status(self.no_Product_match)
