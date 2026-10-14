from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time


def test_login_valid():

    os.makedirs("screenshots", exist_ok=True)

    driver = webdriver.Chrome()

    try:
        driver.get("http://127.0.0.1:5000/login")

        time.sleep(3)

        # Enter registered account details
        driver.find_element(By.ID, "email").send_keys(
            "fatima@test.com"
        )

        driver.find_element(By.ID, "password").send_keys(
            "123456"
        )

        # Click Login
        driver.find_element(
            By.ID,
            "login-btn"
        ).click()

        time.sleep(3)

        # Verify successful login
        assert "/dashboard" in driver.current_url

        # Save screenshot
        result = driver.save_screenshot(
            "screenshots/login_success.png"
        )

        print("Screenshot saved:", result)

    finally:
        driver.quit()
        
   
def test_login_invalid_password():

    driver = webdriver.Chrome()

    driver.get("http://127.0.0.1:5000/login")

    time.sleep(3)

    driver.find_element(
        By.ID,
        "email"
    ).send_keys("wrong@test.com")

    driver.find_element(
        By.ID,
        "password"
    ).send_keys("wrongpassword")

    driver.find_element(
        By.ID,
        "login-btn"
    ).click()

    time.sleep(3)

    # Should remain on login page
    assert "/login" in driver.current_url

    # Check error
    assert "Invalid email or password" in driver.page_source

    driver.save_screenshot(
        "screenshots/login_invalid.png"
    )

    driver.quit()