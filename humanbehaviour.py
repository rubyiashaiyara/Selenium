import random
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


def simulate_human_behavior(driver, num_actions=10):
    print("Simulating human-like behavior...")
    actions = ActionChains(driver)
    for _ in range(num_actions):
        scroll_y = random.randint(100, 800)
        driver.execute_script(f"window.scrollBy(0, {scroll_y});")
        time.sleep(random.uniform(0.5, 2))

    elements = driver.find_elements(By.CSS_SELECTOR, "div")
    for _ in range(num_actions):
        if elements:
            element = random.choice(elements)
            try:
                actions.move_to_element(element).pause(random.uniform(0.5, 2)).perform()
            except:
                pass
    print("Human-like actions completed.")