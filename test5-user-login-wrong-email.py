from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import traceback
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import *
from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.chrome.service import Service
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

        driver.find_element(By.CSS_SELECTOR, 'a[href="/login"]').click()
        time.sleep(2)

        driver.find_element(By.CSS_SELECTOR, 'input[data-qa="login-email"]').send_keys("aahilqali@gmail.com")
        driver.find_element(By.CSS_SELECTOR, 'input[data-qa="login-password"]').send_keys("baababab")

        # Click the login button
        driver.find_element(By.CSS_SELECTOR, 'button[data-qa="login-button"]').click()
        time.sleep(3)


        wait = WebDriverWait(driver, 10)
        submit_button = driver.find_element(By.XPATH,"//button[@type='submit']")
        submit_button.click()
        html = driver.find_element(By.TAG_NAME,'html')
        html.send_keys(Keys.END)

        error_element = driver.find_element(By.XPATH, "//p[@style='color: red;']")
        error_text = error_element.text.strip()

        assert error_text == "Your email or password is incorrect!", f"Expected error not shown, found: {error_text}"
        print("✅ Assertion Passed: Duplicate email error shown correctly.")

    except AssertionError as ae:
        print("❌ Assertion failed:", str(ae))

    except (NoSuchElementException,ElementNotVisibleException,ElementNotSelectableException) as e:
        print(str(e))
    except Exception as e:
        print("Some error occured"+ str(e))
        traceback.print_exc()
    finally:
        time.sleep(3)
        driver.quit()