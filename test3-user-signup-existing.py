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

        wait = WebDriverWait(driver, 10)
        submit_button = driver.find_element(By.XPATH,"//button[@type='submit']")
        submit_button.click()
        html = driver.find_element(By.TAG_NAME,'html')
        html.send_keys(Keys.END)

        error_element = driver.find_element(By.XPATH, "//p[@style='color: red;']")
        error_text = error_element.text.strip()

        assert error_text == "Email Address already exist!", f"Expected error not shown, found: {error_text}"
        print("✅ Assertion Passed: Duplicate email error shown correctly.")

    except AssertionError as ae:
        print("❌ Assertion failed:", str(ae))
    except (NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException) as e:
        print(str(e))
    except Exception as e:
        print("Some error occurred: " + str(e))
        traceback.print_exc()
    finally:
        time.sleep(3)
        driver.quit()
