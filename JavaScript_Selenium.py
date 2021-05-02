from selenium import webdriver
from selenium.webdriver import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://www.amazon.in/')
driver.implicitly_wait(5)
# best_sellers = driver.find_element(By.LINK_TEXT, 'Best Sellers')
# driver.execute_script("arguments[0].click();", best_sellers)
# driver.implicitly_wait(3)
#
# print(driver.execute_script("return document.title;"))
# driver.execute_script("history.go(0);")
# driver.execute_script("alert('helle selenuim');")
# driver.switch_to.alert.accept()


# print(driver.execute_script("return document.documentElement.innerText;"))
#driver.execute_script("arguments[0].style.border = '3px solid red';", best_sellers)
#to scroll to bottom of the page
#driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#t scroll to top of the page
#driver.execute_script("window.scrollTo(document.body.scrollHeight, 0);")

# deals_Of_the_day = driver.find_element(By.XPATH, "//span[text()='Up to 70% off | Bestselling accessories & office supplies']")
# driver.execute_script("arguments[0].scrollIntoView(true);", deals_Of_the_day)
print(driver.execute_script("return navigator.userAgent;"))
#driver.quit()
