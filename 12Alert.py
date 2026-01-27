'''
Docstring for 12Alert
In this program, I learn how to handle pop up alert
'''

import time
from selenium import webdriver
from selenium.webdriver.common.by import By

name = input("Enter the Name : ")

driver = webdriver.Chrome()

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

driver.maximize_window()

driver.find_element(By.CSS_SELECTOR, "input[id='name']").send_keys(name)
driver.find_element(By.ID, "alertbtn").click()

time.sleep(5)

alert = driver.switch_to.alert

alertmsg = alert.text

alert.accept()
time.sleep(5)

print(alertmsg)