'''
Docstring for 8AutoSuggestDropDown

In this program I learn Auto Suggest Drop Down , By using Different Method
'''

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")

driver.maximize_window()

driver.find_element(By.CSS_SELECTOR, "input[id='autosuggest']").send_keys('ind')
time.sleep(5)
countries = driver.find_elements(By.CSS_SELECTOR, "li[class*='ui-menu-item'] a")
time.sleep(5)

for country in countries:
    if country.text == 'India':
        country.click()
        break
time.sleep(5)