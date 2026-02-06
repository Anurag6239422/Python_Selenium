'''
Docstring for 24ScrollDown

In this program I learn how to Scroll down in a website.
'''

from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.implicitly_wait(5)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()

time.sleep(5)
driver.execute_script("window.scrollTo(0,600)")
time.sleep(5)
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")