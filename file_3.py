from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)  

driver = webdriver.Chrome(options=chrome_options) 
driver.maximize_window() 
driver.get("https://www.google.com/")


page_source = driver.page_source
print("page source = ",page_source)

title = driver.title
print("Title = ",title)

current_url = driver.current_url
print("current_url = ",current_url)

window_position = driver.get_window_position(windowHandle='current')
print("window Position = ",window_position)

window_rect = driver.get_window_rect()
print("window react = ",window_rect)

window_size = driver.get_window_size()
print("window size = ",window_size)

driver.minimize_window()

driver.close()