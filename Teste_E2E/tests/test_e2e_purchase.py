import sys
import os
import time

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.confirmation_page import ConfirmationPage

PAUSE = 2


class TestE2EPurchase:

    def test_login_invalido(self, driver):
        login = LoginPage(driver)
        login.open()
        time.sleep(PAUSE)
        login.login("wrong_user", "wrong_pass")
        time.sleep(PAUSE)
        error = login.get_error_message()
        assert "Username and password do not match" in error

    def test_fluxo_completo(self, driver):
        #Login
        login = LoginPage(driver)
        login.open()
        time.sleep(PAUSE)
        login.login("standard_user", "secret_sauce")
        time.sleep(PAUSE)

        #Adicionar produtos ao carrinho
        inventory = InventoryPage(driver)
        assert inventory.is_loaded()
        time.sleep(PAUSE)
        inventory.add_all_products()
        time.sleep(PAUSE)

        #Navega direto ao carrinho (evita popup do Chrome)
        driver.get("https://www.saucedemo.com/cart.html")
        time.sleep(PAUSE)

        #Verifica carrinho e vai ao checkout
        cart = CartPage(driver)
        assert cart.get_item_count() > 0
        time.sleep(PAUSE)
        cart.proceed_to_checkout()
        time.sleep(PAUSE)

        #Preenche dados pessoais
        checkout = CheckoutPage(driver)
        checkout.fill_personal_info("Talyson", "Machado", "64000-000")
        time.sleep(PAUSE)
        checkout.finish_purchase()
        time.sleep(PAUSE)

        #Confirma pedido
        confirmation = ConfirmationPage(driver)
        assert confirmation.is_order_confirmed(), "Compra não foi confirmada"
        time.sleep(PAUSE)
