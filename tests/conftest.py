from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
import pytest
from page_objects.db_base_page import DButils
import config


# @pytest.fixture(params=['chrome'])
@pytest.fixture()
def driver(request):
    # browser = request.param #Multi Browser
    browser = request.config.getoption("--browser")
    print(f"Creating {browser} Driver")
    if browser == "chrome":
        my_driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    elif browser == "firefox":
        my_driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    else:
        raise TypeError(f"Expected 'chrome' or 'firefox' but got {browser}")
    my_driver.maximize_window()
    if config.implicit_wait:
        my_driver.implicitly_wait(config.wait_time)
    yield my_driver
    if config.database_execute:
        DButils.close_connection()
        print("Closing Database Connection")
    print(f"Closing {browser} Driver")
    my_driver.quit()


def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="chrome", help="Browser to execute tests on chrome or firefox"
    )
