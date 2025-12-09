from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import csv


chrome_options = Options()
driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()
driver.get("https://www.flipkart.com/")
time.sleep(2)

searchbar = driver.find_element(By.XPATH,'//*[@id="container"]/div/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/header/div[1]/div[2]/form/div/div/input')
searchbar.send_keys("laptop", Keys.ENTER)
time.sleep(2.1)

laptopnamerow = driver.find_elements(By.CSS_SELECTOR,'._75nlfW')
print(len(laptopnamerow))

# Open CSV file for writing
with open('laptops.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Product Name', 'Product Link', 'Image Link'])
    
    # Loop through each laptop and write data
    for laptop in laptopnamerow:
        laptoplinks = laptop.find_element(By.XPATH, './/a')
        laplink = laptoplinks.get_attribute('href')
        
        productimages = laptop.find_elements(By.TAG_NAME, 'img')
        imageLink = productimages[0].get_attribute('src') if productimages else ''
        
        productname = laptop.find_element(By.XPATH, './/a/div[2]/div[1]/div[1]').text
        
        # Write row to CSV
        writer.writerow([productname, laplink, imageLink])
        
        
        print("------------------------------")
        print("Product Name:", productname)
        print("Product Link:", laplink)
        print("Image Link:", imageLink)


