import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestWomenTopsCategory(unittest.TestCase):
    """
    TC_013: Verify product list displays for Women category → Tops
    Steps:
      1. Navigate to Products page.
      2. In the category sidebar, click 'Women'.
      3. Then click 'Tops' sub-category.
      4. Assert at least one product is shown.
    """

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, 10)
        self.driver.maximize_window()
    def test_TC_015_product_search_invalid(self):
        """TC_015: Searching 'xyz123' shows 'No Products Found'."""
        driver, wait = self.driver, self.wait
        driver.get("https://www.automationexercise.com/products")

        inp = wait.until(EC.element_to_be_clickable((By.ID, "search_product")))
        inp.clear()
        inp.send_keys("xyz123")
        wait.until(EC.element_to_be_clickable((By.ID, "submit_search"))).click()

        msg = wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//*[contains(text(),'No Products Found')]")))
        self.assertTrue(msg.is_displayed(),
                        "Expected 'No Products Found' message for invalid search term")


    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
