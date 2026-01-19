'''
Docstring for 7StaticDropDown
For this program we learn how selenium handle static drop down.
In Inspect if we see select for drop down it means it is a static
'''

import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://rahulshettyacademy.com/angularpractice/")

driver.maximize_window()

driver.find_element(By.CLASS_NAME, "form-control ng-pristine ng-invalid ng-touched").send_keys("Anurag Sandilya")
driver.find_element(By.CSS_SELECTOR, "input[name='email']").send_keys("helloworld@gmail.com")
