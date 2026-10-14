from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time


ADMIN_EMAIL = "admin@bashashare.com"
ADMIN_PASSWORD = "admin123"


def test_admin_access():

    os.makedirs("screenshots", exist_ok=True)

    driver = webdriver.Chrome()

    try:

        driver.get(
            "http://127.0.0.1:5000/login"
        )

        time.sleep(1)

        driver.find_element(
            By.ID, "email"
        ).send_keys(ADMIN_EMAIL)

        driver.find_element(
            By.ID, "password"
        ).send_keys(ADMIN_PASSWORD)

        driver.find_element(
            By.ID, "login-btn"
        ).click()

        time.sleep(2)

        driver.get(
            "http://127.0.0.1:5000/admin"
        )

        time.sleep(2)

        assert "/admin" in driver.current_url

        assert "Admin Panel" in driver.page_source

        driver.save_screenshot(
            "screenshots/admin_panel.png"
        )

    finally:
        driver.quit()