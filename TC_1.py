from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import traceback
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

if __name__ == '__main__':
    try:
        chrome_options = Options()
        chrome_options.add_argument(r"user-data-dir=C:\Users\Administrator\AppData\Local\Google\Chrome\User Data")
        chrome_options.add_argument("profile-directory=Profile 1")

        driver = webdriver.Chrome()
        driver.get("https://www.automationexercise.com/")
        wait = WebDriverWait(driver, 10)
        driver.maximize_window()

        # Go to Signup/Login page
        driver.find_element(By.CSS_SELECTOR, 'a[href="/login"]').click()
        time.sleep(2)

        # Fill signup name and email
        driver.find_element(By.CSS_SELECTOR, 'input[data-qa="signup-name"]').send_keys("Aahil")
        driver.find_element(By.CSS_SELECTOR, 'input[data-qa="signup-email"]').send_keys("aahilashiqali@gmail.com")
        driver.find_element(By.CSS_SELECTOR, 'button[data-qa="signup-button"]').click()
        time.sleep(3)

        # Click Mr. radio button
        driver.find_element(By.ID, "id_gender1").click()

        # Fill password and other fields
        driver.find_element(By.ID, "password").send_keys("TestPassword123")
        driver.find_element(By.ID, "first_name").send_keys("Aahil")
        driver.find_element(By.ID, "last_name").send_keys("Aahil")
        driver.find_element(By.ID, "address1").send_keys("Blessings")

        # Select country from dropdown
        Select(driver.find_element(By.ID, "country")).select_by_visible_text("India")

        # Fill remaining fields
        driver.find_element(By.ID, "state").send_keys("Sindh")
        driver.find_element(By.ID, "city").send_keys("Karachi")
        driver.find_element(By.ID, "zipcode").send_keys("74550")
        driver.find_element(By.ID, "mobile_number").send_keys("0352512345")

        # Scroll to bottom
        html = driver.find_element(By.TAG_NAME, 'html')
        html.send_keys(Keys.END)

        # Wait for the Create Account button to be clickable, then click
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@data-qa='create-account']"))
        )
        submit_button.click()

        # Optional: Wait for confirmation
        time.sleep(3)
        assert "ACCOUNT CREATED!" in driver.page_source.upper()

    except (NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException) as e:
        print(str(e))
    except Exception as e:
        print("Some error occurred: " + str(e))
        traceback.print_exc()
    finally:
        time.sleep(3)
        driver.quit()
