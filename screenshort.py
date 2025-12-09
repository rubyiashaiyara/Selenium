import os 
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from datetime import datetime


chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
driver.maximize_window()


driver.get("https://www.google.com/")
now = datetime.now()
current_time = now.strftime("%H_%M_%S")
driver.save_screenshot(os.getcwd()+'/screenshots/Screenshot_'+current_time+'.png')


driver.get("https://www.facebook.com/")
now = datetime.now()
current_time = now.strftime("%H_%M_%S")
driver.save_screenshot(os.getcwd()+'/screenshots/Screenshot_'+current_time+'.png')