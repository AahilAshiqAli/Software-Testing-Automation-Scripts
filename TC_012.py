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

    def test_TC_012_signup_mandatory_fields(self):
        # Steps:
        # 1. Navigate to Signup page
        # 2. Enter name and email, then click 'Signup'
        # 3. Leave mandatory fields empty and click 'Create Account'
        # Assert:
        #   Validation errors are shown and account is not created
        driver = self.driver
        wait = self.wait

        driver.get("https://www.automationexercise.com/signup")
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[data-qa='signup-name']"))).send_keys("Test User")
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[data-qa='signup-email']"))).send_keys("")
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-qa='signup-button']"))).click()

        # On the form that follows, leave mandatory fields (e.g. password/address) blank:
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-qa='create-account']"))).click()

        # Expect HTML5 required validation on first mandatory field (e.g. password)
        pwd_field = wait.until(EC.visibility_of_element_located((By.ID, "password")))
        validation_msg = driver.execute_script("return arguments[0].validationMessage;", pwd_field)
        self.assertTrue(validation_msg, "Expected a validation message for missing mandatory fields")
    def tearDown(self):
        time.sleep(1000000000)
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
