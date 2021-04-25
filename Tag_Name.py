from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)

driver.get('https://www.amazon.in/')
totalLinks = driver.find_elements(By.TAG_NAME,'a')

print(len(totalLinks))

for i in totalLinks:
    print(i.get_attribute('href'))
    print(i.text)

totalImage = driver.find_elements(By.TAG_NAME, 'img')
print(len(totalImage))

for ele in totalImage:
    print(ele.get_attribute('src'))
driver.quit()
