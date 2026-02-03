'''
Docstring for 18SumValidation
In this program , I learn Sum Validation 
'''

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.implicitly_wait(5)

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.maximize_window()

driver.find_element(By.CLASS_NAME, "search-keyword").send_keys("ber")

values = driver.find_elements(By.XPATH, "//div[@class='product']")

for value in values:
    value.find_element(By.XPATH, "div/button").click()

driver.find_element(By.XPATH, "//img[@alt='Cart']").click()

driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()

amounts = driver.find_elements(By.CSS_SELECTOR, "tr td:nth-child(5) p")
sum = 0

for amount in amounts:
    sum = sum + int(amount.text)

print(sum)

assert sum == int(driver.find_element(By.CSS_SELECTOR, "span[class='totAmt']").text)

promotion_code = input("Enter the Promo Code : ")

if promotion_code == 'rahulshettyacademy' :
    driver.find_element(By.CLASS_NAME, "promoCode").send_keys(promotion_code)
    driver.find_element(By.CLASS_NAME, "promoBtn").click()
    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "promoCode")))
    msg = driver.find_element(By.CLASS_NAME, "promoInfo").text
    assert msg == 'Code applied ..!'
    print(msg)
else:
    driver.find_element(By.CLASS_NAME, "promoCode").send_keys(promotion_code)
    driver.find_element(By.CLASS_NAME, "promoBtn").click()
    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "promoCode")))
    msg = driver.find_element(By.CLASS_NAME, "promoInfo").text
    assert not msg == 'Code applied ..!'
    print(msg)

driver.find_element(By.XPATH, "//button[text()='Place Order']").click()

