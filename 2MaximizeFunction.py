#In This Program I learn how browser is maximize
from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get("https://rahulshettyacademy.com")
driver.maximize_window()

time.sleep(2)

print(driver.current_url)
print(driver.title)

