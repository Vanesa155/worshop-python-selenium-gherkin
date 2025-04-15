from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class InventoryPage(BasePage):

    INVENTORY_TITLE = (By.CSS_SELECTOR, '[data-test="title"]')
    PRODUCT_NAMES = (By.CSS_SELECTOR, '[data-test="inventory-item-name"]')
    PRODUCT_PRICES = (By.CSS_SELECTOR, '[data-test="inventory-item-price"]')
    ADD_TO_CART_BUTTON = (By.ID, "add-to-cart-sauce-labs-backpack")
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")

    def go_to_cart(self):
        """Navega al carrito de compras"""
        self.click(self.CART_LINK)

    def is_inventory_page_displayed(self):
        """Verifica si el usuario está en la página de inventario."""
        return self.is_element_visible(self.INVENTORY_TITLE)

    def add_product_to_the_cart(self):
        self.click(self.ADD_TO_CART_BUTTON)
       
    