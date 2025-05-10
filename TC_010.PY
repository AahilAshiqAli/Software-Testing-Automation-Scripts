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

    def test_password_field_is_masked(self):
        driver = self.driver
        wait = self.wait

        # 1. Navigate to Login page
        driver.get("https://www.automationexercise.com/login")

        # 2. Enter a valid email to populate the form
        email_input = wait.until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "input[data-qa='login-email']")))
        email_input.clear()
        email_input.send_keys("existing_user@example.com")

        # 3. Locate the password input by its data-qa attribute
        pwd_input = wait.until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "input[data-qa='login-password']")))

        # 4. Enter a sample password
        pwd_input.clear()
        sample_password = "ValidPass123"
        pwd_input.send_keys(sample_password)

        # 5. Verify the field’s type is 'password' (masked)
        input_type = pwd_input.get_attribute("type")
        self.assertEqual(input_type, "password",
                         f"Expected input type 'password', but got '{input_type}'")
        # Optionally, ensure that the underlying value matches what was sent
        entered_value = pwd_input.get_attribute("value")
        self.assertEqual(entered_value, sample_password,
                         "Password input did not receive the entered value.")

    def tearDown(self):
        time.sleep(1000000000)
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
