from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from webdriver_manager.firefox import GeckoDriverManager

#Chrome
# options = Options()
# options.add_argument('--allow-running-insecure-content')
# options.add_argument('--ignore-certificate-errors')

# desired_capabilitites = DesiredCapabilities().CHROME.copy()
# desired_capabilitites['acceptInsecureCerts'] = True
# driver = webdriver.Chrome(ChromeDriverManager().install(), desired_capabilities=desired_capabilitites)
# driver.implicitly_wait(5)
# driver.get('https://expired.badssl.com/')

#Firefox
# profile = webdriver.FirefoxProfile()
# profile.accept_untrusted_certs=True

desired_capabilities = DesiredCapabilities.FIREFOX.copy()
desired_capabilities['acceptInsecurecerts'] = True
#driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(), firefox_profile=profile)
driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(), capabilities=desired_capabilities)
driver.get('https://expired.badssl.com/')
print(driver.find_element(By.TAG_NAME, 'h1').text)

driver.quit()
