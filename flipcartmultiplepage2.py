from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv
import time


chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()

search_keyword = "smart watches"

for page_number in range(1,6):
    driver.get(f"https://www.flipkart.com/search?q={search_keyword}&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page={page_number}")

    WebDriverWait(driver, 20).until(
        lambda d: d.execute_script("return document.readyState") == "complete"
    )
    time.sleep(3)
    
driver.quit()
