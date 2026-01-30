'''
Docstring for 17ExplicitWait
In this program we learn explicit wait, for explicit we wait for a perticular operation only
'''

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.implicitly_wait(5)  #Global Wait

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.maximize_window()

driver.find_element(By.CLASS_NAME, "search-keyword").send_keys("ber")

products = driver.find_elements(By.XPATH, "//div[@class='product']")

for product in products:
    product.find_element(By.XPATH, "div/button").click()

driver.find_element(By.XPATH, "//img[@alt='Cart']").click()

driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()

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