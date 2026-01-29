'''
Docstring for 15ImplicitWait
In Implicit Wait behave as normal wait but if it findout the result under the given time period in that case it will ignore the remaining time period.

for example : driver.implicitly_wait(5)
if it findout the result in 1 second in that case it will ignore remaining 4 second and move to the next line
'''

import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()


driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.maximize_window()

driver.implicitly_wait(5)

driver.find_element(By.CLASS_NAME, "search-keyword").send_keys("ber")

time.sleep(5) #Implicit wait does not work for list. It is an exceptional

results = driver.find_elements(By.XPATH, "//div[@class='product']")

for result in results:
    result.find_element(By.XPATH, "div/button").click()
#    result.implicitly_wait(10) #AttributeError: 'WebElement' object has no attribute 'implicitly_wait'
    time.sleep(5)

driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']").click()

driver.implicitly_wait(10)

driver.find_element(By.XPATH,"//button[text()='PROCEED TO CHECKOUT']").click()

driver.implicitly_wait(10)

promo_code = input("Enter the Promo Code : ")
driver.find_element(By.CLASS_NAME, "promoCode").send_keys(promo_code)

driver.implicitly_wait(10)

driver.find_element(By.CLASS_NAME, "promoBtn").click()

driver.implicitly_wait(10)

message = driver.find_element(By.XPATH, "//span[text()='Code applied ..!']").text

assert message == "Code applied ..!"

time.sleep(5)

driver.find_element(By.XPATH, "//button[text()='Place Order']").click()

time.sleep(5)
