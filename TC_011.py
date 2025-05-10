import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time 
class TestPasswordMasking(unittest.TestCase):
    """
    TC_010: Verify password field is masked during login
    Steps:
      1. Navigate to Login page.
      2. Enter valid email to ensure page state.
      3. Locate the password input.
      4. Enter a sample password.
      5. Assert that its HTML type attribute is 'password'.
    """

    def setUp(self):
        # Launch Chrome (ensure chromedriver is in your PATH)
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, 10)

    def test_TC_011_login_incorrect_password(self):
        # Steps:
        # 1. Navigate to Login page
        # 2. Enter valid email and incorrect password
        # 3. Click 'Login' button
        # Assert:
        #   Error message 'Your email or password is incorrect!' is displayed
        driver = self.driver
        wait = self.wait

        driver.get("https://www.automationexercise.com/login")
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[data-qa='login-email']"))).send_keys("existing_user@example.com")
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[data-qa='login-password']"))).send_keys("WrongPass123")
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-qa='login-button']"))).click()

        error = wait.until(EC.visibility_of_element_located((By.XPATH, "//*[contains(text(), 'Your email or password is incorrect!')]")))
        self.assertTrue(error.is_displayed(), "Expected incorrect login error message")

    def tearDown(self):
        time.sleep(1000000000)
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
