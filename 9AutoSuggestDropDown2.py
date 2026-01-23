'''
Docstring for 9AutoSuggestDropDown2
This Program Print whatever we selected from Drop Down
'''

import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
driver.maximize_window()
time.sleep(5)

driver.find_element(By.ID, "autosuggest").send_keys("ind")
time.sleep(5)
countries = driver.find_elements(By.CSS_SELECTOR, "li[class ='ui-menu-item'] a")
time.sleep(5)
for country in countries:
    if country.text == 'India':
        country.click()
        break

print(driver.find_element(By.ID, "autosuggest").get_attribute("value"))

assert driver.find_element(By.ID, "autosuggest").get_attribute("value") == 'India'

