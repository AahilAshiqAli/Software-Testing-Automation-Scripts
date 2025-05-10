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

    def test_TC_013_women_category_products(self):
        driver = self.driver
        wait = self.wait

        driver.get("https://www.automationexercise.com/products")

        # Click on 'Women' category
        women_category = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[text()='Women']")))
        women_category.click()

        # Click on 'Tops' sub-category
        tops_subcategory = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[text()='Tops ']")))
        tops_subcategory.click()

        # Assert that at least one product is displayed
        products = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "product-image-wrapper")))
        self.assertGreater(len(products), 0, "No products found in Women → Tops category.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
