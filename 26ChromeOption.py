'''
Docstring for 26ChromeOption
We have to use Chrome Option
'''

from selenium import webdriver

driver = webdriver.Chrome()

driver.implicitly_wait(5)

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")

chrome_option = webdriver.ChromeOptions()
chrome_option.add_argument("--start-maximized")
