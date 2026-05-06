import time
from faker import Faker
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.confirmation_page import ConfirmationPage

PAUSE = 5 
fake = Faker()

class TestE2EPurchase:

    def test_successful_login(self, driver):
        login = LoginPage(driver)
        login.open()
        login.login("standard_user", "secret_sauce")
        time.sleep(PAUSE)
        inventory = InventoryPage(driver)
        assert inventory.is_loaded(), "Login falhou: página de inventário não carregou"

    def test_invalid_login(self, driver):
        login = LoginPage(driver)
        login.open()
        login.login("wrong_user", "wrong_pass")
        time.sleep(PAUSE)
        error = login.get_error_message()
        assert "Username and password do not match" in error

    def test_add_products_to_cart(self, driver):
        LoginPage(driver).open()
        LoginPage(driver).login("standard_user", "secret_sauce")
        time.sleep(PAUSE)
        inventory = InventoryPage(driver)
        inventory.add_all_products()
        time.sleep(PAUSE)
        assert inventory.get_cart_count() > 0, "Nenhum produto foi adicionado ao carrinho"

    def test_full_purchase_flow(self, driver):
        login = LoginPage(driver)
        login.open()
        login.login("standard_user", "secret_sauce")
        time.sleep(PAUSE)

        inventory = InventoryPage(driver)
        assert inventory.is_loaded()
        inventory.add_specific_products(["Sauce Labs Backpack", "Sauce Labs Bike Light"])
        time.sleep(PAUSE)
        inventory.go_to_cart()
        time.sleep(PAUSE)

        cart = CartPage(driver)
        assert cart.is_loaded()
        assert cart.get_item_count() == 2
        cart.proceed_to_checkout()
        time.sleep(PAUSE)

        checkout = CheckoutPage(driver)
        first_name = "Talyson"
        last_name = "Machado"
        postal_code = fake.postcode()
        print(f"\nDados gerados: {first_name} {last_name}, CEP {postal_code}")
        checkout.fill_personal_info(first_name, last_name, postal_code)
        time.sleep(PAUSE)
        checkout.finish_purchase()
        time.sleep(PAUSE)

        # Confirmar pedido
        confirmation = ConfirmationPage(driver)
        assert confirmation.is_order_confirmed(), "Compra não foi confirmada"