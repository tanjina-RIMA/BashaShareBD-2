from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time


EMAIL = "YOUR_REGISTERED_EMAIL"
PASSWORD = "YOUR_CORRECT_PASSWORD"


def test_logout():

    os.makedirs("screenshots", exist_ok=True)

    driver = webdriver.Chrome()

    try:

        driver.get("http://127.0.0.1:5000/login")

        driver.find_element(
            By.ID, "email"
        ).send_keys(EMAIL)

        driver.find_element(
            By.ID, "password"
        ).send_keys(PASSWORD)

        driver.find_element(
            By.ID, "login-btn"
        ).click()

        time.sleep(2)

        driver.get(
            "http://127.0.0.1:5000/logout"
        )

        time.sleep(2)

        assert "/login" in driver.current_url

        driver.save_screenshot(
            "screenshots/logout.png"
        )

    finally:
        driver.quit()
        
def test_dashboard_without_login():

    os.makedirs("screenshots", exist_ok=True)

    driver = webdriver.Chrome()

    try:

        driver.get(
            "http://127.0.0.1:5000/dashboard"
        )

        time.sleep(2)

        assert "/login" in driver.current_url

        driver.save_screenshot(
            "screenshots/dashboard_protection.png"
        )

    finally:
        driver.quit()
        
def test_add_listing_without_login():

    os.makedirs("screenshots", exist_ok=True)

    driver = webdriver.Chrome()

    try:

        driver.get(
            "http://127.0.0.1:5000/add-listing"
        )

        time.sleep(2)

        assert "/login" in driver.current_url

        driver.save_screenshot(
            "screenshots/add_listing_protection.png"
        )

    finally:
        driver.quit()
        
