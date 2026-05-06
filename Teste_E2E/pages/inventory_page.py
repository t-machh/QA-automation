import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class InventoryPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def is_loaded(self):
        return "inventory" in self.driver.current_url

    def add_all_products(self):
        add_buttons = self.driver.find_elements(By.CSS_SELECTOR, "button.btn_inventory")
        for button in add_buttons:
            if button.text == "Add to cart":
                button.click()

    def add_specific_products(self, product_names):
        for product_name in product_names:
            xpath = f"//div[@class='inventory_item']//div[text()='{product_name}']/ancestor::div[@class='inventory_item']//button"
            self.wait.until(EC.element_to_be_clickable((By.XPATH, xpath))).click()

    def get_cart_count(self):
        cart_badge = self.driver.find_elements(By.CLASS_NAME, "shopping_cart_badge")
        if cart_badge:
            return int(cart_badge[0].text)
        return 0

    def go_to_cart(self):
        # Aguarda o ícone do carrinho estar clicável
        cart_icon = self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "shopping_cart_link")))
        # Rola até o elemento para garantir visibilidade
        self.driver.execute_script("arguments[0].scrollIntoView(true);", cart_icon)
        time.sleep(0.3)
        try:
            cart_icon.click()
        except:
            self.driver.execute_script("arguments[0].click();", cart_icon)
        self.wait.until(EC.url_contains("cart.html"))