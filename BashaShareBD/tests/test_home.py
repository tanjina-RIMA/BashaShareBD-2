from selenium import webdriver
import os
import time


def test_homepage():

    # Create screenshots folder if it doesn't exist
    os.makedirs("screenshots", exist_ok=True)

    driver = webdriver.Chrome()

    try:
        driver.get("http://127.0.0.1:5000/")

        time.sleep(2)

        # Check homepage content
        assert "BashaShare" in driver.page_source

        # Save screenshot
        driver.save_screenshot(
            "screenshots/homepage_test.png"
        )

    finally:
        driver.quit()