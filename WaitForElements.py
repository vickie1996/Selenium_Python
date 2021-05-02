from selenium import webdriver
from selenium.webdriver import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://www.freshworks.com/')
wait = WebDriverWait(driver, 10)

elements_list = wait.until(ec.presence_of_all_elements_located((By.CSS_SELECTOR, 'ul.footer-nav li')))
print(len(elements_list))

for ele in elements_list:
    print(ele.text)

driver.quit()   
