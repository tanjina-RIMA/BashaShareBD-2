from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time


EMAIL = "fatima@test.com"
PASSWORD = "123456"


def login(driver):

    driver.get("http://127.0.0.1:5000/login")
    time.sleep(1)

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

def test_add_listing():

   def test_add_listing():

    os.makedirs("screenshots", exist_ok=True)

    driver = webdriver.Chrome()

    try:

        login(driver)

        driver.get(
            "http://127.0.0.1:5000/add-listing"
        )

        time.sleep(2)

        print("ADD LISTING URL:", driver.current_url)

        title = driver.find_element(By.ID, "title")
        title.send_keys("Selenium Test Flat")

        location = driver.find_element(By.ID, "location")
        location.send_keys("Mirpur")

        rent = driver.find_element(By.ID, "rent")
        rent.send_keys("15000")

        description = driver.find_element(By.ID, "description")
        description.send_keys(
            "Test accommodation for SQT project"
        )

        print("TITLE VALUE:", title.get_attribute("value"))
        print("LOCATION VALUE:", location.get_attribute("value"))
        print("RENT VALUE:", rent.get_attribute("value"))
        print(
            "DESCRIPTION VALUE:",
            description.get_attribute("value")
        )

        form_valid = driver.execute_script("""
            return document.querySelector("form").checkValidity();
        """)

        print("FORM VALID:", form_valid)

        submit_button = driver.find_element(
            By.ID, "add-listing-btn"
        )

        print(
            "SUBMIT BUTTON DISPLAYED:",
            submit_button.is_displayed()
        )

        print(
            "SUBMIT BUTTON ENABLED:",
            submit_button.is_enabled()
        )

        submit_button.click()

        time.sleep(3)

        print("AFTER SUBMIT URL:", driver.current_url)
        print("AFTER SUBMIT PAGE:", driver.page_source)

        driver.save_screenshot(
            "screenshots/after_submit.png"
        )

        assert "/listings" in driver.current_url

    finally:
        driver.quit()

def test_view_listings():

    os.makedirs("screenshots", exist_ok=True)

    driver = webdriver.Chrome()

    try:

        login(driver)

        driver.get(
            "http://127.0.0.1:5000/listings"
        )

        time.sleep(2)

        assert "Available Accommodations" in driver.page_source

        driver.save_screenshot(
            "screenshots/view_listings.png"
        )

    finally:
        driver.quit()


def test_search_listing():

    os.makedirs("screenshots", exist_ok=True)

    driver = webdriver.Chrome()

    try:

        login(driver)

        driver.get(
            "http://127.0.0.1:5000/listings"
        )

        time.sleep(1)

        driver.find_element(
            By.ID, "search"
        ).send_keys("Mirpur")

        driver.find_element(
            By.ID, "search-btn"
        ).click()

        time.sleep(2)

        assert "Mirpur" in driver.page_source

        driver.save_screenshot(
            "screenshots/search_listing.png"
        )

    finally:
        driver.quit()
