'''
Docstring for 10CheckBox
In this program, I learn how to handle checkbox
'''

import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()

options = driver.find_elements(By.XPATH, "//input[@type='checkbox']")
time.sleep(5)

for option in options:
    if option.get_attribute("value") ==  "Option2":
        option.click()
        assert option.is_selected()
        break