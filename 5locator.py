'''
Docstring for 5locator
In this program I am learning how to use radio button in selenium using css selector locator.
'''

import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()

driver.find_element(By.NAME, "email").send_keys("hello@gmail.com")
time.sleep(5)
driver.find_element(By.ID, "exampleInputPassword1").send_keys("123456")
time.sleep(5)
driver.find_element(By.CLASS_NAME, "form-check-input").click()
time.sleep(5)
driver.find_element(By.CSS_SELECTOR, "input[value='option2']").click()
time.sleep(5)
driver.find_element(By.XPATH, "//input[@type='date']").send_keys("26-12-1999")
time.sleep(5)
driver.find_element(By.XPATH, "//input[@type='submit']").click()
time.sleep(5)
driver.find_element(By.XPATH, "(//input[@type='text'])[3]").send_keys("My Name is khan")
time.sleep(5)


message = driver.find_element(By.CLASS_NAME, "alert-success").text

print(message)

assert "Success" in message


