import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time 
class SignupInvalidEmailTest(unittest.TestCase):
    """
    TC_009 Verify signup with invalid email format:
    1. Navigate to Signup page.
    2. Enter name and invalid email (e.g., 'user@').
    3. Click 'Signup' button.

    Expected: Form does not submit; validation error for email format is shown.
    """

    def setUp(self):
        # Initialize Chrome WebDriver (ensure chromedriver is in PATH)
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 10)

    def test_invalid_email_signup(self):
        driver = self.driver
        wait = self.wait

        # 1. Navigate to home page
        driver.get("https://www.automationexercise.com/")

        # 2. Click 'Signup / Login' link
        signup_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Signup / Login")))
        signup_link.click()

        # 3. Fill in name and invalid email
        name_input = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[data-qa='signup-name']")))
        email_input = driver.find_element(By.CSS_SELECTOR, "input[data-qa='signup-email']")
        name_input.send_keys("Test User")
        email_input.send_keys("user@")

        # 4. Click 'Signup' button
        signup_button = driver.find_element(By.CSS_SELECTOR, "button[data-qa='signup-button']")
        signup_button.click()

        # 5. Assert validation error is shown
        # Using HTML5 validation message from the email input
        validation_message = email_input.get_attribute('validationMessage')
        self.assertTrue(validation_message, "Expected validation message for invalid email, but got none.")

    def tearDown(self):
        # Close browser
        time.sleep(1000000)
        self.driver.quit()



if __name__ == '__main__':
    unittest.main()
