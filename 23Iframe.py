'''
Docstring for 23Iframe
'''

from selenium import webdriver


driver = webdriver.Chrome()
driver.implicitly_wait(5)

driver.get("https://the-internet.herokuapp.com/iframe")
driver.maximize_window()

driver.switch_to.frame("mce_0_ifr")

driver.find_element(By.CL)