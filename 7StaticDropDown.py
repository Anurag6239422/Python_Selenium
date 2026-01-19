'''
Docstring for 7StaticDropDown
For this program we learn how selenium handle static drop down.
In Inspect if we see select for drop down it means it is a static
'''

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()

driver.get("https://rahulshettyacademy.com/angularpractice/")

driver.maximize_window()

driver.find_element(By.CLASS_NAME, "form-control").send_keys("Anurag Sandilya")
time.sleep(5)
driver.find_element(By.CSS_SELECTOR, "input[name='email']").send_keys("helloworld@gmail.com")
time.sleep(5)
driver.find_element(By.ID, "exampleInputPassword1").send_keys("Bokaro@123")
time.sleep(5)
driver.find_element(By.XPATH, "//input[@type='checkbox']").click()
time.sleep(5)
dropdown = Select(driver.find_element(By.ID, "exampleFormControlSelect1"))
time.sleep(5)
dropdown.select_by_index(1)
time.sleep(5)
dropdown.select_by_visible_text('Male')
time.sleep(5)
driver.find_element(By.CSS_SELECTOR, "input[id='inlineRadio2']").click()
time.sleep(5)
driver.find_element(By.NAME, "bday").send_keys("26-12-1999")
time.sleep(5)
driver.find_element(By.XPATH, "//input[@type='submit']").click()
time.sleep(5)
driver.find_element(By.XPATH, "(//input[@type='text'])[3]").send_keys("Bye")
time.sleep(5)
