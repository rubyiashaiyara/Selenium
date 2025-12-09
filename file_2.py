from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)  

driver = webdriver.Chrome(options=chrome_options) 
driver.maximize_window() #tp make screen larger
driver.get("https://www.google.com/")


#XPATH
# input = driver.find_element(By.XPATH,'/html/body/div[2]/div[4]/form/div[1]/div[1]/div[1]/div[1]/div[2]/textarea')
# input.send_keys("Facebook")

#class name
#input = driver.find_element(By.CLASS_NAME,'gLFyf').send_keys("facebook")
#search = driver.find_element(By.XPATH, '/html/body/div[2]/div[4]/form/div[1]/div[1]/div[3]/center/input[1]').click()

#tag name
# input = driver.find_element(By.TAG_NAME,'textarea').send_keys("whatsapp")
# search = driver.find_element(By.XPATH, '/html/body/div[2]/div[4]/form/div[1]/div[1]/div[3]/center/input[1]').click()

# Partial Link Text
#driver.find_element(By.PARTIAL_LINK_TEXT,'Gmail').click()

#image
#driver.find_element(By.PARTIAL_LINK_TEXT,'Images').click()

# partial link text
#Gmail = driver.find_element(By.LINK_TEXT,'Gmail').click()

#id
#driver.find_element(By.ID,'')

#css seletor
#driver.find_element(By.CSS_SELECTOR,'')