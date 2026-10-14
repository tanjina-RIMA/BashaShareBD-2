from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import uuid


def test_register_valid_user():

    driver = webdriver.Chrome()

    driver.get("http://127.0.0.1:5000/register")

    time.sleep(1)

    # Create unique email
    unique_email = f"test{uuid.uuid4().hex[:8]}@test.com"

    # Enter data
    driver.find_element(By.ID, "name").send_keys(
        "Selenium Test User"
    )

    driver.find_element(By.ID, "email").send_keys(
        unique_email
    )

    driver.find_element(By.ID, "phone").send_keys(
        "01712345678"
    )

    driver.find_element(By.ID, "password").send_keys(
        "password123"
    )

    # Click register
    driver.find_element(
        By.ID,
        "register-btn"
    ).click()

    time.sleep(2)

    # Check redirect
    assert "/login" in driver.current_url

    driver.save_screenshot(
        "screenshots/register_success.png"
    )

    driver.quit()
 