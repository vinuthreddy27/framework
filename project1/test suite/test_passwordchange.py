from project1.POM.homepage import HomePage


def test_password_change(get_browser):
    homepage=HomePage(get_browser)
    login_page=homepage.click_on_login_link()
    landing_page=login_page.login_into_application()
    password_page=landing_page.click_on_password_link()
    password_page.change()
    assert landing_page.success_message()