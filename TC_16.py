import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestProductDetailsPage(unittest.TestCase):
    """
    TC_016: Verify that clicking 'View Product' on the first item shows the product details page.
    Steps:
      1. Navigate to Products page.
      2. Click on 'View Product' of the first product.
      3. Assert that product details are displayed.
    """

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, 10)
        self.driver.maximize_window()

    def test_TC_016_product_details_page(self):
        driver = self.driver
        wait = self.wait

        driver.get("https://www.automationexercise.com/products")

        # Click on 'View Product' of the first product
        view_product = wait.until(EC.element_to_be_clickable((By.XPATH, "(//a[text()='View Product'])[1]")))
        view_product.click()

        # Assert that product details are displayed
        product_name = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@class='product-information']/h2")))
        self.assertTrue(product_name.is_displayed(), "Product name is not displayed on the product details page.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
