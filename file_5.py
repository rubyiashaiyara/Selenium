#flipcart practise
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)  

driver = webdriver.Chrome(options=chrome_options) 
driver.maximize_window() 
driver.get("https://www.flipkart.com/skyberg-60-litres-curve-water-resistant-rucksack-hiking-trekking-travel-unisex-l-backpack/p/itm1bb187e5d1af8?pid=BKPH8MTHNYA2NWFC&lid=LSTBKPH8MTHNYA2NWFCRQYDZT&marketplace=FLIPKART&q=bag&store=search.flipkart.com&srno=s_1_3&otracker=search&otracker1=search&fm=Search&iid=e86c31b4-76c5-44a0-9d30-97558e97deb1.BKPH8MTHNYA2NWFC.SEARCH&ppt=sp&ppn=sp&ssid=tf8w6ly7jk0000001761546971665&qH=4a82715423d654d6")


for i in range(2,26):
    bag_name_element = driver.find_element('xpath','/html/body/div/div/div[3]/div[1]/div[2]/div[{0}]/div/div[{0}]/div/div/a[1]'.format(i))
    bag_name = bag_name_element.text
    print("Bag Name = ",bag_name)

    current_price = driver.find_element('xpath','/html/body/div[1]/div/div[3]/div[1]/div[2]/div[{0}]/div/div[{0}]/div[1]/div/div[1]'.format(i))
    current_price = current_price.text
    print("Current Price = ",current_price)

    mrp_price = driver.find_element('xpath','/html/body/div[1]/div/div[3]/div[1]/div[2]/div[{0}]/div/div[{0}]/div[1]/div/div[2]'.format(i))
    m_p = mrp_price.text
    print("mrp =",m_p)

    discount_element = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[3]/div[1]/div[2]/div[{0}]/div/div[{0}]/div[1]/div/div[3]/span'.format(i))
    discount = discount_element.text
    print("Discount = ",discount)


    # stars_element = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div[1]/div[2]/div[2]/div/div[4]/div/div/span[1]/div'.format(i))
    # stars = stars_element.text
    # print('Starts =',stars)

    # rating_review = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div[1]/div[2]/div[2]/div/div[4]/div/div/span[2]/span')
    # rat = rating_review.text
    # print('Rating =',rat)