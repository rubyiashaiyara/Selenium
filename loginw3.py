from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


chrome_options = Options()
chrome_options.add_experimental_option("detach",True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=chrome_options)
driver.maximize_window()
driver.get("https://www.w3schools.com/")

wait = WebDriverWait(driver, 5)

sign_in_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="tnb-login-btn"]')))
sign_in_btn.click()

email = "22103043@iubat.edu"
password = "Rabonti@111"

email_element = driver.find_element(By.XPATH,'//*[@id="tnb-login-dropdown-email"]')
email_element.send_keys(email)

password = driver.find_element(By.XPATH,'//*[@id="tnb-login-dropdown-password"]')
password.send_keys(password)

# log_in = driver.find_element(By.XPATH,'//*[@id="loginFormElement"]/button')
# log_in.click()



submit_button = wait.until(EC.presence_of_element_located((By.XPATH, '//button[@type="submit"]')))
driver.execute_script("arguments[0].click();", submit_button)