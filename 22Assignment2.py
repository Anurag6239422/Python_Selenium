'''
Docstring for 22Assignment2
In this program I do the assignment which is assigned by the udemy
'''

import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(5)

driver.get("https://rahulshettyacademy.com/documents-request")

msg = driver.find_element(By.XPATH, "//a[text()='mentor@rahulshettyacademy.com']").text

academy = msg.strip().split("@")[1].split(".")[0]

driver.get("https://rahulshettyacademy.com/loginpagePractise/")

driver.find_element(By.XPATH, "//input[@id='username']").send_keys(academy)
driver.find_element(By.XPATH, "//input[@id='password']").send_keys("Bokaro@123")
driver.find_element(By.XPATH, "//input[@id='signInBtn']").click()

alert = driver.switch_to.alert

alertmsg = alert.text

alert.accept()
time.sleep(5)

print(alertmsg)