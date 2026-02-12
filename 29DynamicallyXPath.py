'''
Docstring for 29DynamicallyXPath
In this program, I learn how to create XPath Dynamically 
'''

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(10)

fruit = "Banana"

driver.get("https://rahulshettyacademy.com/upload-download-test/index.html")
driver.maximize_window()

price_number = driver.find_element(By.XPATH, "//div[text()='Price']").get_attribute("data-column-id") 
print(driver.find_element(By.XPATH, "//div[text()='"+fruit+"']/parent::div/parent::div/div[@id='cell-"+price_number+"-undefined']").text)