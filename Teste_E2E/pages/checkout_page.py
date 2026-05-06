import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def fill_personal_info(self, first_name, last_name, postal_code):
        # Aguarda os campos estarem visíveis
        self.wait.until(EC.presence_of_element_located((By.ID, "first-name"))).send_keys(first_name)
        self.driver.find_element(By.ID, "last-name").send_keys(last_name)
        self.driver.find_element(By.ID, "postal-code").send_keys(postal_code)

        # Rola até o botão "Continue" para garantir que está visível
        continue_btn = self.driver.find_element(By.ID, "continue")
        self.driver.execute_script("arguments[0].scrollIntoView(true);", continue_btn)
        time.sleep(0.5)  

        continue_btn.click()

        # Aguarda a navegação para a página de overview 
        self.wait.until(EC.url_contains("checkout-step-two"))

    def finish_purchase(self):
        # Aguarda o botão "Finish" estar clicável e então clica
        self.wait.until(EC.element_to_be_clickable((By.ID, "finish"))).click()