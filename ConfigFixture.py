import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

@pytest.fixture(params=['Chrome', 'firefox'], scope='class')
def init_drivers(request):
    if request.param == 'Chrome':
        web_driver = webdriver.Chrome(ChromeDriverManager().install())

    if request.param == 'firefox':
        web_driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())

        request.cls.driver = web_driver
        web_driver.implicitly_wait(5)

        yield
        web_driver.close()
