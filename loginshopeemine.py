import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time, os, random, json
from dotenv import load_dotenv
from humanbehaviour import simulate_human_behavior

load_dotenv()
mail = os.getenv('mail')
password = os.getenv('password')

COOKIES_FILE = "shopee_seller.json"
BASE_URL = "https://shopee.sg/"

options = uc.ChromeOptions()
options.add_argument("--disable-blink-features=AutomationControlled")

with uc.Chrome(options=options) as driver:   #  context manager handles cleanup
    driver.maximize_window()
    wait = WebDriverWait(driver, 15)

    # --- Function definitions go inside or before ---
    def load_cookies():
        if not os.path.exists(COOKIES_FILE):
            print("No cookie file found, logging in manually...")
            return False
        try:
            driver.get(BASE_URL)
            with open(COOKIES_FILE, "r") as f:
                cookies = json.load(f)
            for c in cookies:
                cookie = {
                    "name": c.get("name"),
                    "value": c.get("value"),
                    "domain": c.get("domain"),
                    "path": c.get("path", "/"),
                    "secure": c.get("secure", False),
                    "httpOnly": c.get("httpOnly", False),
                }
                if c.get("expiry"):
                    cookie["expires"] = int(c["expiry"])
                try:
                    driver.execute_cdp_cmd("Network.setCookie", cookie)
                except Exception:
                    try:
                        driver.add_cookie({"name": cookie["name"], "value": cookie["value"]})
                    except:
                        pass
            driver.refresh()
            print("Cookies loaded successfully!")
            time.sleep(3)
            return True
        except Exception as e:
            print("Failed to load cookies:", e)
            return False

    def save_cookies():
        try:
            cookies = driver.get_cookies()
            with open(COOKIES_FILE, "w") as f:
                json.dump(cookies, f, indent=2)
            print(f"Cookies saved to {COOKIES_FILE}")
        except Exception as e:
            print("Failed to save cookies:", e)

    # --- Start ---
    driver.get(BASE_URL)
    time.sleep(2)

    if not load_cookies():
        try:
            print("Logging in with credentials...")
            user_field = wait.until(EC.presence_of_element_located((By.NAME, "loginKey")))
            user_field.send_keys(mail)
            time.sleep(random.uniform(1, 2))
            pass_field = wait.until(EC.presence_of_element_located((By.NAME, "password")))
            pass_field.send_keys(password)
            time.sleep(random.uniform(1, 2))
            pass_field.send_keys(Keys.RETURN)
            print("Login submitted...")
            time.sleep(8)
        except Exception as e:
            print("Login failed or form not found:", e)

    
    simulate_human_behavior(driver,3)
    
    driver.get("https://shopee.sg/search?keyword=bag")
    time.sleep(8)
       
    driver.get("https://shopee.sg/Food-Beverages-cat.11011871")
    time.sleep(8)
    
    simulate_human_behavior(driver,2)

    print(" Done! Closing in 5 seconds...")
    time.sleep(5)
