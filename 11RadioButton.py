'''
Docstring for 11RadioButton
In this Program, I learn how to handle the radio buttom
'''

import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

driver.maximize_window()

buttons = driver.find_elements(By.XPATH, "//input[@type='radio']")

for button in buttons:
    if button.get_attribute("value") == "Radio2":
        button.click()
        time.sleep(5)
        assert button.is_selected()
        break


assert driver.find_element(By.ID, "displayed-text").is_displayed()

time.sleep(5)

driver.find_element(By.ID, "hide-textbox").click()

assert not driver.find_element(By.ID, "displayed-text").is_displayed()

time.sleep(5)