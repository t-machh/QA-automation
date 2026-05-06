from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ConfirmationPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def is_order_confirmed(self):
        header = self.wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, "complete-header"))
        )
        return "Thank you" in header.text