from selenium import webdriver
import time 

driver = webdriver.Edge()

driver.get("https://www.google.com/")
#driver.quit() # for close browser
time.sleep(10)