import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.headless = True
driver = webdriver.Chrome(ChromeDriverManager().install(), options= options)

driver.get("https://www.amazon.in/")
'''one page screenshot'''
driver.get_screenshot_as_file('Amazonss.png')

'''full screenshot you are running in headless mode'''
S = lambda X: driver.execute_script('return document.body.parentNode.scroll'+X)
driver.set_window_size(S('Width'), S('Height'))
driver.find_element_by_tag_name('body').screenshot('newsc.png')

driver.quit()
