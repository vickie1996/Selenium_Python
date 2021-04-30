import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://cgi-lib.berkeley.edu/ex/fup.html')
driver.implicitly_wait(5)

#type=file should be there else as the UI dev to add 
driver.find_element(By.NAME, 'upfile').send_keys('C:/Users/vivek/matchesNew.csv')

driver.find_element(By.XPATH, "//input[@type='submit']").click()
time.sleep(3)
driver.quit()
