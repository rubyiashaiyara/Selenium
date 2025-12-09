import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import os
from dotenv import load_dotenv
import random

 
load_dotenv()

mail = os.getenv('mail')
password = os.getenv('pass')

chrome_options = Options()
chrome_options.add_experimental_option("detach",True)
driver = webdriver.Chrome(options=chrome_options)

driver.maximize_window()
driver.get("https://shopee.sg/")

wait = WebDriverWait(driver, 5)
sing_in_btn = WebDriverWait(driver,20).until(
    EC.element_to_be_clickable((By.XPATH,'//*[@id="main"]/div/div[2]/div/div[2]/div/div/div/div[2]/div/div[2]/form/div[1]/div[1]/input'))
    )
#time.sleep(random.uniform(1,3))
sing_in_btn.click()
sing_in_btn.send_keys(mail)
psw = WebDriverWait(driver,20).until(
    EC.element_to_be_clickable((By.XPATH,'//*[@id="main"]/div/div[2]/div/div[2]/div/div/div/div[2]/div/div[2]/form/div[2]/div[1]/input'))
)
time.sleep(random.uniform(1,3))
psw.click()
psw.send_keys(password)
login = WebDriverWait(driver,20).until(
    EC.element_to_be_clickable((By.XPATH,'//*[@id="main"]/div/div[2]/div/div[2]/div/div/div/div[2]/div/div[2]/form/button'))
)
time.sleep(random.uniform(1,3))
login.click()

time.sleep(15)

driver.quit()