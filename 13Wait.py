'''
Docstring for 13Wait
In this program we learn wait Logic
'''

import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")

driver.maximize_window()

driver.find_element(By.CLASS_NAME, "search-keyword").send_keys("ber")
time.sleep(5)

result = driver.find_elements(By.XPATH, "//div[@class='product']")

print(len(result))
print(result)