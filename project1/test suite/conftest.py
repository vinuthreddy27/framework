import pytest
from selenium import webdriver

from project1.configurations.config import TestData


@pytest.fixture(params=["chrome"],scope="function")
def get_browser(request):
    global driver
    if request.param=="chrome":
        driver=webdriver.Chrome()

    elif request.param == "firefox":
        driver = webdriver.Firefox()

    elif request.param == "edge":
        driver = webdriver.Edge()

    else:
        print("valid browser")

    driver.get(TestData.base_url)
    driver.maximize_window()
    driver.delete_all_cookies()
    yield driver
    driver.quit()
