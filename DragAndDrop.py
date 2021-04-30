from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(5)

driver.get('https://jqueryui.com/resources/demos/droppable/default.html')
source = driver.find_element(By.ID, 'draggable')
target = driver.find_element(By.ID, 'droppable')

act_item = ActionChains(driver)

#Drag and Drop using single method
#act_item.drag_and_drop(source, target).perform()

#using single steps
act_item.click_and_hold(source).move_to_element(target).release().perform()
driver.quit()
