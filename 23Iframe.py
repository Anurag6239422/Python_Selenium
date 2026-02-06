'''
Docstring for 23Iframe
'''

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome()
driver.implicitly_wait(5)

driver.get("https://the-internet.herokuapp.com/iframe")
driver.maximize_window()

driver.switch_to.frame("mce_0_ifr")

# Clear using JavaScript instead of .clear()
element = driver.find_element(By.CLASS_NAME, "mce-content-body")
driver.execute_script("arguments[0].innerHTML = '';", element)


time.sleep(5)

# Type the text
driver.find_element(By.XPATH, "//body[@id ='tinymce']").send_keys("My Name is Anurag and I am a QA Engineer")