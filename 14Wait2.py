'''
Docstring for 14Wait2
Through this program we learn multiple wait 1.Implicit and 2. Explicit
'''

import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")

driver.maximize_window()

driver.find_element(By.CLASS_NAME, "search-keyword").send_keys("ber")

results = driver.find_elements(By.XPATH, "//div[@class='product']")

for result in results:
#    result.find_element(By.XPATH, "//div[@class='product']//div//button").click()
    result.find_element(By.XPATH, "div/button").click()
    time.sleep(5)

driver.find_element(By.XPATH, "//img[@alt='Cart']").click()
time.sleep(5)
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()
time.sleep(5)
driver.find_element(By.CLASS_NAME, "promoCode").send_keys("AnuragSandilya")
time.sleep(5)
driver.find_element(By.XPATH, "//button[text()='Apply']").click()
time.sleep(5)
driver.find_element(By.XPATH, "//button[text()='Place Order']").click()
time.sleep(5)