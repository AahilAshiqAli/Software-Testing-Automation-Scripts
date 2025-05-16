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

       # Check if the price is displayed and assertion passed
        price_element = wait.until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(), 'Rs.')]")))
        price_text = price_element.text
        assert "Rs." in price_text, "Price not found in the expected format."
        print("Price found:", price_text)
        
        # Check if the "Add to cart" button is visible and then click it
        add_to_cart_button = driver.find_element(By.XPATH, "//button[contains(@class, 'btn') and contains(@class, 'btn-default') and contains(@class, 'cart')]")

        assert add_to_cart_button.is_displayed(), "'Add to cart' button is not displayed."
        print("✅ Add to cart button is visible.")
        
        # Click the "Add to cart" button
        add_to_cart_button.click()
        
        # Wait for some confirmation or page change (adjust as necessary for the specific flow)
        time.sleep(3)  # Add a delay to simulate real user interaction
        
        # Check if a success message or confirmation is shown (this will depend on the site's behavior)
        # Example: check for a cart update or a confirmation message after adding to the cart
        cart_message = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='cart-message']")))  # This is an example path
        assert "success" in cart_message.text.lower(), "Failed to add item to cart."
        print("Item successfully added to cart.")



    except (NoSuchElementException,ElementNotVisibleException,ElementNotSelectableException) as e:
        print(str(e))
    except Exception as e:
        print("Some error occured"+ str(e))
        traceback.print_exc()
    finally:
        time.sleep(3)
        driver.quit()