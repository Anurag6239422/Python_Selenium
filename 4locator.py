'''
Docstring for 4locator:
In this program I learn different location like XPath
There are different locator like:
XPath, CSSSelector, Id, Name, Classname
'''

import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()


driver.find_element(By.NAME, "email").send_keys("hello@gmail.com")
driver.find_element(By.ID, "exampleInputPassword1").send_keys("123456")
driver.find_element(By.ID, "exampleCheck1").click()
driver.find_element(By.XPATH, '//input[@type="submit"]').click()

message = driver.find_element(By.CLASS_NAME, "alert-success").text

time.sleep(10)

print(message)

assert "Success" in message
