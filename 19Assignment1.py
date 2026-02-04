'''
Docstring for 19Assignment1
In this program , I am doing whatever the assignment which is given by the udemy course.
'''

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

#Assignment

driver = webdriver.Chrome()

driver.implicitly_wait(5)

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.maximize_window()

driver.find_element(By.CLASS_NAME, "search-keyword").send_keys('ber')
time.sleep(2)

products = driver.find_elements(By.CSS_SELECTOR,"h4[class='product-name']")


product_list = []

for product in products:
    product_list.append(product.text)

print(product_list)

#Assignment 2

values = driver.find_elements(By.XPATH, "//div[@class='product']")

for value in values:
    value.find_element(By.XPATH, "div/button").click()

driver.find_element(By.XPATH, "//img[@alt='Cart']").click()

driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()

driver.find_element(By.CLASS_NAME, "promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CLASS_NAME, "promoBtn").click()

wait = WebDriverWait(driver, 10)
wait.until(EC.text_to_be_present_in_element((By.CLASS_NAME, "promoInfo"), "Code applied ..!"))

sum = driver.find_element(By.CLASS_NAME, "totAmt").text

discount = driver.find_element(By.CLASS_NAME, "discountAmt").text

print("Total Cost of Vegetable : ", sum)
print("Final Cost of Vegetable after Discount : ", discount)

assert sum > discount