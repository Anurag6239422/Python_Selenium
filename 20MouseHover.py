'''
Docstring for 20MouseHover
In this program, I am learning Mouse Hover
'''

import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(5)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

driver.maximize_window()

action = ActionChains(driver, 10)

time.sleep(5)
action.move_to_element(driver.find_element(By.XPATH, "//button[@id='mousehover']")).perform()
action.context_click(driver.find_element(By.LINK_TEXT, "Top")).perform()
