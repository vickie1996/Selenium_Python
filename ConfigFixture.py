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

        
        
        #another file which is using above file to get the Chrome and firefox launed using Fixture parameterizing
        
        import pytest
from selenium.webdriver.common.by import By

@pytest.mark.usefixtures('init_drivers')
class BaseTest:
    pass

class Test_FB(BaseTest):

    @pytest.mark.parametrize(
                                "username, password",
                                [
                                    ('vivekberwal','admin123'),
                                    ('vivek', 'admins1254')
                                ]
                            )

    def test_login(self,username, password):
        self.driver.get("https://www.facebook.com/")
        self.driver.find_element(By.ID, 'email').send_keys(username)
        self.driver.find_element(By.ID, 'pass').send_keys(password)



