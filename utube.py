from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
import time

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
driver.maximize_window()

driver.get("https://www.youtube.com/")

search_box = driver.find_element(By.XPATH, '//*[@id="center"]/yt-searchbox/div[1]/form/input')
search_box.send_keys('food')
search_box.send_keys(Keys.ENTER)

WebDriverWait(driver, 15).until(
    lambda d: d.execute_script("return document.readyState") == "complete"
)

time.sleep(5)

# Scroll down and up to load more videos
for i in range(3):
    driver.execute_script('window.scrollBy(0, 800);')
    time.sleep(2)

for i in range(3):
    driver.execute_script('window.scrollBy(0, -800);')
    time.sleep(2)

videos = driver.find_elements(By.TAG_NAME, 'ytd-video-renderer')
print(f"Total videos found: {len(videos)}")

video_data = []

for video in videos:
    try:
        # Video title and link
        title_element = video.find_element(By.ID, 'video-title')
        title = title_element.text
        link = title_element.get_attribute('href')

        # Channel name
        try:
            channel_element = video.find_element(By.XPATH, './/ytd-channel-name//a')
            channel_name = channel_element.text
        except:
            channel_name = "Unknown Channel"

        # Views
        try:
            views_element = video.find_element(By.XPATH, './/span[@class="inline-metadata-item style-scope ytd-video-meta-block"]')
            views = views_element.text
        except:
            views = "No view info"

        video_data.append({
            "Title": title,
            "Channel": channel_name,
            "Views": views,
            "Link": link
        })
    except Exception as e:
        print(f"Skipping one video due to: {e}")

# Print results
print("\nAll video details:\n")
for info in video_data:
    print(f"Title: {info['Title']}")
    print(f"Channel: {info['Channel']}")
    print(f"Views: {info['Views']}")
    print(f"Link: {info['Link']}\n")
    
    
driver.quit()
