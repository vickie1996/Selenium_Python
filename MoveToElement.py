from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
import time
driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get('https://www.spicejet.com/')
driver.implicitly_wait(10)

login_ele = driver.find_element(By.ID, 'ctl00_HyperLinkLogin')
## Move to element when we have to hover over the web page for some particular values

act_item = ActionChains(driver)

act_item.move_to_element(login_ele).perform()

spice_club_members_ele = driver.find_element(By.LINK_TEXT, 'SpiceClub Members')
act_item.move_to_element(spice_club_members_ele).perform()

driver.find_element(By.LINK_TEXT, 'Member Login').click()
time.sleep(4)

driver.quit()
