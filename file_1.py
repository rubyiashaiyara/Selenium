from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)  

driver = webdriver.Chrome(options=chrome_options) 
driver.maximize_window() 
driver.get("https://www.google.com/")

