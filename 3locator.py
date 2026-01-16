'''
Docstring for 3locator
In this program, I Learn how to insert email id , password by using locator.\
locator are : CSSSelector, Xpath, id, name, classname, linktext
'''

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://rahulshettyacademy.com/angularpractice/")

driver.maximize_window()

driver.find_element(By.NAME, "email").send_keys("hello@gmail.com")
driver.find_element(By.ID, "exampleInputPassword1").send_keys("1223456")
driver.find_element(By.ID, "exampleCheck1").click()

time.sleep(2)