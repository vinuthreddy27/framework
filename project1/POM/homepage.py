from project1.POM.gift_page import Gift_page
from project1.POM.loginpage import LoginPage
from project1.POM.logout_page import Logout_page
from project1.POM.product_page import ProductPage
from project1.POM.registerpage import Register_page
from project1.POM.wishlist_page import wishlist_page
from project1.library.basepage import BasePage


class HomePage(BasePage):
    my_Account_link=("xpath","//a[normalize-space()='My Account']")
    login_link=("xpath","//a[normalize-space()='Login']")
    register_locator = ("xpath", "//a[.='Register']")
    login_locator = ("xpath", "//a[.='Login']")

    search_tf = ("name", "search")
    btn = ("css selector", "span[class='input-group-btn']")

    wishlist = ("xpath", "//span[contains(.,'Wish List')]")

    logout_btn = ("xpath", "//ul[@class='dropdown-menu dropdown-menu-right']/..//a[.='Logout']")

    gift_locator = ("xpath", "//a[.='Gift Certificates']")

    contact_us_locator = ("xpath", "//a[.='Contact Us']")

    cart_link = ("id", "wishlist-total")

    cart_total = ("css selector", "*[id='cart']")
    shopping_cart = ("css selector", "a[title='Shopping Cart']")
    downloads_link = ("xpath", "//li[@class='dropdown']//li[.='Downloads']")
    transactions_link = ("xpath", "//li[@class='dropdown']//li[.='Transactions']")
    order_history_link = ("xpath", "//li[@class='dropdown']//li[.='Order History']")
    logout_link = ("xpath", "//ul[starts-with(@class,'dropdown')]//a[.='Logout']")

    def homepage_register(self):
        self.click_on_element(self.my_Account_link)
        self.click_on_element(self.register_locator)

        register_page=Register_page(self.driver)
        return register_page


    def Send_product(self, product):
        self.send_keys_on_element(self.search_tf, product)
        self.click_on_element(self.btn)

        product_page=ProductPage(self.driver)
        return product_page

    def click_giftlink(self):
        self.click_on_element(self.gift_locator)

        page_gift=Gift_page(self.driver)
        return page_gift

    def wish_link(self):
        self.click_on_element(self.wishlist)

        wish_page = wishlist_page(self.driver)
        return wish_page

    def click_on_logout(self):
        self.click_on_element(self.my_Account_link)
        self.click_on_element(self.logout_link)

        page_logout=Logout_page(self.driver)
        return page_logout

    def click_on_login_link(self):
       self.click_on_element(self.my_Account_link)
       self.click_on_element(self.login_link)

       login_page=LoginPage(self.driver)
       return login_page


