from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class InventoryPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def is_loaded(self):
        self.wait.until(EC.url_contains("inventory"))
        return "inventory" in self.driver.current_url

    def add_all_products(self):
        self.wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "btn_inventory")))
        buttons = self.driver.find_elements(By.CLASS_NAME, "btn_inventory")
        for btn in buttons:
            self.wait.until(EC.element_to_be_clickable(btn))
            btn.click()

    def go_to_cart(self):
        self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "shopping_cart_link"))).click()

    def get_cart_count(self):
        badge = self.driver.find_elements(By.CLASS_NAME, "shopping_cart_badge")
        return int(badge[0].text) if badge else 0
