'''
Docstring for 25Sorting
In this Program I learn how to sort the items
'''

import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.implicitly_wait(5)

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.maximize_window()

driver.find_element(By.LINK_TEXT, "Top Deals").click()

windowsOpened = driver.window_handles
driver.switch_to.window(windowsOpened[1])

driver.find_element(By.XPATH, "//span[text()='Veg/fruit name']").click()


veggie = driver.find_elements(By.XPATH, "//tr//td[1]")

veggie_item = []
for item in veggie:
    veggie_item.append(item.text)

copy_veggie_item = veggie_item.copy()

copy_veggie_item.sort()

assert veggie_item == copy_veggie_item