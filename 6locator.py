'''
Docstring for 6locator
In this program I learn about to test link website
'''

import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://rahulshettyacademy.com/client/")

driver.maximize_window()

driver.find_element(By.LINK_TEXT, "Forgot password?").click()
time.sleep(5)
driver.find_element(By.XPATH,"//input[@type='email']").send_keys("HelloWorld@gmail.com")
time.sleep(5)
driver.find_element(By.ID, "userPassword").send_keys("Bokaro@123")
time.sleep(5)
driver.find_element(By.CSS_SELECTOR, "input[id='confirmPassword']").send_keys("Bokaro@123")
time.sleep(5)
driver.find_element(By.XPATH, "//button[@type='submit']").click()
time.sleep(5)