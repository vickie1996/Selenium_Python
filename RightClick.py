from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(5)
'''right/Context click'''

driver.get('https://swisnl.github.io/jQuery-contextMenu/demo.html')
rightClick_ele = driver.find_element(By.XPATH,"//span[text()='right click me']")
act_items = ActionChains(driver)
act_items.context_click(rightClick_ele).perform()           #for doing right click use contect_click in ActionChains

optionList = driver.find_elements(By.CSS_SELECTOR, 'li.context-menu-item')
for ele in optionList:
    print(ele.text)
    if ele.text == 'Cut':
        ele.click()
        break
        
driver.quit()
