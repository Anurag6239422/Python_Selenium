'''
Docstring for 31EndToEndPractice

In this program, I am going to test end to end project using selenium
'''

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.implicitly_wait(5) 

driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()

driver.find_element(By.NAME, "name").send_keys("Anurag Sandilya") #Here, using Name Locator
driver.find_element(By.CSS_SELECTOR, "input[name='email']").send_keys("anuragsandilya1996@gmail.com")
driver.find_element(By.XPATH, "//input[@type='password']").send_keys("Bokaro@123")
driver.find_element(By.XPATH, "//label[text()='Check me out if you Love IceCreams!']").click()
#In this line, I am learning dropdown
dropdown=Select(driver.find_element(By.ID, "exampleFormControlSelect1"))
dropdown.select_by_visible_text("Female")

driver.find_element(By.CSS_SELECTOR, "label[for='inlineRadio1']").click()
driver.find_element(By.CSS_SELECTOR, "input[name='bday']").send_keys("26/12/1999")
driver.find_element(By.XPATH, "//input[@type='submit']").click()

msg = driver.find_element(By.CLASS_NAME, "alert-success").text
assert "Success" in msg

driver.find_element(By.XPATH,"//a[text()='Shop']").click()

phones=[]
phones = driver.find_elements(By.XPATH, "//div[@class='card h-100']")

driver.execute_script("window.scrollTo(0,4000)")

for phone in phones:
    phone_name = phone.find_element(By.XPATH, "div/h4/a").text
    if phone_name == 'Blackberry':
      driver.execute_script("window.scrollTo(0,1200)")
      phone.find_element(By.XPATH, "div/button").click()


driver.find_element(By.CSS_SELECTOR, "a[class*=btn-primary]").click()
driver.find_element(By.XPATH, "//button[@class='btn btn-success']").click()
driver.find_element(By.XPATH, "//input[@id='country']").send_keys("ind")

wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.XPATH, "//a[text()='India']")))

driver.find_element(By.XPATH, "//a[text()='India']").click()
driver.find_element(By.CLASS_NAME, "checkbox-primary").click()
driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()
success_msg = driver.find_element(By.CLASS_NAME, "alert-success").text

assert "Success! Thank you!" in success_msg

time.sleep(10)

driver.close() #end up the test and clear the session