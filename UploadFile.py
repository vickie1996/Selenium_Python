from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
import time
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get('https://www.techlistic.com/p/selenium-practice-form.html')
driver.implicitly_wait(10)
driver.maximize_window()
driver.find_element(By.NAME, "firstname").send_keys("Vivek")
driver.find_element(By.NAME, "lastname").send_keys("Berwal")
driver.find_element(By.XPATH, "//input[@value='Male']").click()
driver.find_element(By.XPATH, "//input[@value='3']").click()
driver.find_element(By.XPATH, "//input[@id='datepicker']").send_keys("5/20/2022")
driver.find_element(By.XPATH, "//input[@value='Automation Tester']").click()
driver.find_element(By.XPATH, "//input[@value='Selenium Webdriver']").click()

#sel = Select(driver.find_element(By.))

#Image Upload
imageUpload = driver.find_element(By.XPATH, "//input[@name='photo']")
imageUpload.send_keys("C:/Users/vivek/OneDrive/Pictures/Saved Pictures/About.png")

driver.find_element(By.XPATH, "//button[@name='submit']").click()

time.sleep(20)