import pytest

from project1.POM.homepage import HomePage
from project1.utilities.excel_reader import get_data_from_excel


def test_login(get_browser):
    homepage=HomePage(get_browser)
    login_page=homepage.click_on_login_link()
    landing_page=login_page.login_into_application()
    assert landing_page.proper_message()

@pytest.mark.parametrize("email,password",get_data_from_excel("C:/Users/Vinuthreddy/Documents/Book9.xlsx","Sheet1"))
def test_login2(get_browser,email,password):
    homepage = HomePage(get_browser)
    login_page = homepage.click_on_login_link()
    landing_page=login_page.login(email,password)
    assert landing_page.proper_message()
