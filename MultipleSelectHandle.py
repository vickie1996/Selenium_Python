import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.support.ui import Select


driver = webdriver.Chrome(ChromeDriverManager().install())


def multiple_drop(list, value):
    if value[0] == 'all':
        try:
            for ele in list:
                ele.click()
        except Exception as e:
            print(e)
    else:
        for ele in list:
            print(ele.text)
            for k in range(len(value)):
                if ele.text == value[k]:
                    ele.click()
                    break

driver.get('https://www.jqueryscript.net/demo/Drop-Down-Combo-Tree/')
driver.find_element(By.ID, 'justAnInputBox').click()
time.sleep(2)
optionlist = driver.find_elements(By.CSS_SELECTOR, 'span.comboTreeItemTitle')
#valueList = ['choice 2', 'choice 3', 'choice 6 2 2', 'choice 6 2 3']   # to select more thn 1 option
valueList = ['all']             # to select all options at once
#valueList = ['choice 2']       # to select only 1 option at a time 
print(len(optionlist))
multiple_drop(optionlist,valueList)

