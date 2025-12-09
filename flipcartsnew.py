from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv
import time

# Chrome setup
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.flipkart.com/")
driver.maximize_window()

# Search for "laptop"
search = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME, "q"))
)
search.send_keys("laptop")
search.submit()

# Wait for product cards to load
WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.CSS_SELECTOR, "a.IRpwTa, a.s1Q9rs, div.KzDlHZ"))
)




# Get blocks
products = driver.find_elements(By.CSS_SELECTOR, "div._75nlfW")

# CSV file
with open("flipkart_laptops.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Product Name", "Product Link", "Image Link"])

    for product in products:
        try:
            name_element = product.find_element(By.CSS_SELECTOR, "div.KzDlHZ, a.IRpwTa, a.s1Q9rs")
            name = name_element.text.strip()
        except:
            name = ""

        try:
            link = product.find_element(By.TAG_NAME, "a").get_attribute("href")
        except:
            link = ""

        try:
            image = product.find_element(By.CSS_SELECTOR, "img").get_attribute("src")
        except:
            image = ""

        # Write to CSV
        writer.writerow([name, link, image])

        # Also print 
        print("------------------------------")
        print("Product Name:", name)
        print("Product Link:", link)
        print("Image Link:", image)

# Close browser
time.sleep(3)
driver.quit()

print("\n Data saved successfully to 'flipkart_laptops.csv'")
