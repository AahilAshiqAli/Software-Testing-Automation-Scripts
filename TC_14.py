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
    def test_TC_014_product_search_valid(self):
        """TC_014: Searching 'Dress' returns matching products."""
        driver, wait = self.driver, self.wait
        driver.get("https://www.automationexercise.com/products")

        inp = wait.until(EC.element_to_be_clickable((By.ID, "search_product")))
        inp.clear()
        inp.send_keys("Dress")
        wait.until(EC.element_to_be_clickable((By.ID, "submit_search"))).click()

        results = wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, ".product-image-wrapper")))
        self.assertGreater(len(results), 0,
                           "Expected at least one product matching 'Dress'")

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, 10)
        self.driver.maximize_window()

    
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
