'''
Docstring for 28DownloadUploadFile
In this program , I learn how to upload and download the file
'''

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.implicitly_wait(5)

driver.get("https://rahulshettyacademy.com/upload-download-test/index.html")

driver.find_element(By.ID, "downloadButton").click()

file_path = r"C:\Users\anura_9posmze\Downloads\download.xlsx"

file_input = driver.find_element(By.XPATH, "//input[@id='fileinput']")
file_input.send_keys(file_path)

wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'Updated Excel Data Successfully.')]")))

print(driver.find_element(By.XPATH, "//div[contains(text(),'Updated Excel Data Successfully.')]").text)