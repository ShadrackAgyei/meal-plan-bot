from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
import os

STUDENT_ID = os.environ.get("STUDENT_ID")
URL = "https://subscriber.mplan.ashesi.edu.gh/"

options = Options()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(options=options)

try:
    driver.get(URL)
    time.sleep(2)

    # Step 1: Enter ID and click the gold button
    id_input = driver.find_element(By.CSS_SELECTOR, 'input[type="text"]')
    id_input.send_keys(STUDENT_ID)

    go_button = driver.find_element(By.CSS_SELECTOR, 'button[type="button"]')
    go_button.click()
    time.sleep(3)

    # Step 2: Click "Settings" tab
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC

    # Wait up to 10 seconds for the "Settings" tab to appear
    wait = WebDriverWait(driver, 10)
    settings_tab = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[text()='Settings']")))
    settings_tab.click()


    # Step 3: Click "Pin Change" tile
    driver.find_element(By.XPATH, "//div[contains(text(), 'Pin Change')]").click()
    time.sleep(2)

    # Step 4: Enter ID again
    pin_input = driver.find_element(By.ID, "name")
    pin_input.send_keys(STUDENT_ID)
    time.sleep(1)

    # Step 5: Click the Change Pin button
    change_pin_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Change Pin')]")
    change_pin_button.click()
    time.sleep(2)

    print("✅ Success! Check your email for your new daily PIN.")

finally:
    driver.quit()
