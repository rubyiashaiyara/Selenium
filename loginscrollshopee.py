import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time, os, random, json
from dotenv import load_dotenv
from humanbehaviour import simulate_human_behavior  # ensure this file exists

# --- Load environment variables ---
load_dotenv()
mail = os.getenv('mail')
password = os.getenv('password')

COOKIES_FILE = "shopee_seller.json"
BASE_URL = "https://shopee.sg/"

# --- Chrome options ---
options = uc.ChromeOptions()

# ✅ Use a DUPLICATE of your Profile 13 (named ShopeeProfile)
# Make sure you have copied: 
# C:\Users\USER\AppData\Local\Google\Chrome\User Data\Profile 13
# into a new folder called ShopeeProfile (in the same directory)
options.add_argument(r"--user-data-dir=C:\Users\USER\AppData\Local\Google\Chrome\User Data\Profile 13")

# ⚙️ Recommended stability and anti-detection flags
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("--start-maximized")
options.add_argument("--no-first-run")
options.add_argument("--no-service-autorun")
options.add_argument("--password-store=basic")

# --- Launch Chrome ---
with uc.Chrome(options=options) as driver:
    wait = WebDriverWait(driver, 15)

    # --- Function to load cookies ---
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
                    driver.add_cookie(cookie)
                except Exception as e:
                    print("Failed to add cookie:", e)
                    pass
            driver.refresh()
            print("Cookies loaded successfully!")
            time.sleep(3)
            return True
        except Exception as e:
            print("Failed to load cookies:", e)
            return False

    # --- Start Shopee automation ---
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

    # --- Human-like behavior simulation ---
    simulate_human_behavior(driver, int(random.uniform(1, 5)))

    driver.get("https://shopee.sg/Video-Games-cat.11013478")
    simulate_human_behavior(driver, int(random.uniform(1, 5)))
    
    driver.get("https://shopee.sg/Computers-Peripherals-cat.11013247")
    simulate_human_behavior(driver, int(random.uniform(1, 5)))
    
    driver.get("https://shopee.sg/Mobile-Gadgets-cat.11013350")
    simulate_human_behavior(driver, int(random.uniform(1, 5)))
    
    driver.get("https://shopee.sg/Home-Appliances-cat.11027421")
    simulate_human_behavior(driver, int(random.uniform(1, 5)))
    
    driver.get("https://shopee.sg/Food-Beverages-cat.11011871")
    simulate_human_behavior(driver, int(random.uniform(1, 5)))

    print("Done! Closing in 5 seconds...")
    time.sleep(5)
