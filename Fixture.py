import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = None
@pytest.fixture(scope='module')
def init_driver():
    global driver
    print('---------------------setup------------------')
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(5)
    driver.delete_all_cookies()
    driver.get("https://www.google.com")

    yield
    print('--------------tear down---------------')
    driver.quit()


#@pytest.mark.usefixtures("init_driver")
def test_google_title(init_driver):
    assert driver.title == "Google"

#@pytest.mark.usefixtures("init_driver")
def test_google_ur(init_driver):
    assert driver.current_url == 'https://www.google.com/'
