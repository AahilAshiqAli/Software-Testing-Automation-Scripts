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
from selenium.webdriver.support import expected_conditions as EC

if __name__ == '__main__':
    try:
        chrome_options = Options()
        chrome_options.add_argument(r"user-data-dir=C:\Users\Administrator\AppData\Local\Google\Chrome\User Data")
        chrome_options.add_argument("profile-directory=Profile 1") 

        driver = webdriver.Chrome()
        driver.get("https://www.automationexercise.com/product_details/2")
        wait = WebDriverWait(driver, 10)
        driver.maximize_window()

        driver.find_element(By.ID, "name").send_keys("Aahil")
        driver.find_element(By.ID, "email").send_keys("aahilashiqali")
        driver.find_element(By.ID, "review").send_keys("fantastic")
        wait = WebDriverWait(driver, 10)
        
        driver.find_element(By.ID, 'button-review').click()
        success_element = driver.find_element(By.XPATH, "//div[contains(@class, 'alert-success')]/span")
        success_text = success_element.text.strip()
        assert success_text != "Thank you for your review.", f"Unexpected success message found: {success_text}"
        print("✅ Assertion Passed: Success message is NOT shown as expected.")




    except (NoSuchElementException,ElementNotVisibleException,ElementNotSelectableException) as e:
        print(str(e))
    except Exception as e:
        print("Some error occured"+ str(e))
        traceback.print_exc()
    finally:
        time.sleep(3)
        driver.quit()