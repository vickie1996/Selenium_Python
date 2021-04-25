import time
from selenium.webdriver.common.by import By
from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\Users\\vivek\\OneDrive\\Documents\\Driver\\chromedriver.exe")
driver.get("http:\\www.google.com")

print(driver.title)

driver.find_element(By.NAME, 'q').send_keys("Anythins you want to search")
optionList = driver.find_elements(By.CSS_SELECTOR, 'ul.erkvQe li span')
print(len(optionList))

for i in optionList:
    print(i.text)
    if i.text == 'link which has to be selected':
        i.click()
        break


time.sleep(5)
driver.quit()
