from behave import given, when, then
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from selenium.webdriver.common.by import By

@given('the user is on the login page')
def step_given_user_on_login_page(context):
    context.driver.get("https://www.saucedemo.com")
    context.login_page = LoginPage(context.driver)

@given('the user is on the inventory page')
def step_given_user_on_inventory_page(context):
    context.driver.get("https://www.saucedemo.com/inventory.html")
    context.inventory_page = InventoryPage(context.driver)

@when('the user logs in with valid credentials')
def step_when_user_logs_in_valid(context):
    context.login_page.login("standard_user", "secret_sauce")
    context.inventory_page = InventoryPage(context.driver)

@when('the user logs in with invalid credentials')
def step_when_user_logs_in_invalid(context):
    context.login_page.login("invalid_user", "invalid_password")

@when('the user logs in with empty credentials')
def step_when_user_logs_in_empty(context):
    context.login_page.login("", "")

@when('the user adds an item to the cart')
def step_when_user_adds_item_to_the_cart(context):
    context.inventory_page.add_product_to_the_cart()  

@when('the user should be redirected shopping page and enters their information')
def step_user_proceeds_to_checkout(context):
    context.cart_page = CartPage(context.driver)
    context.cart_page.click_checkout()
    context.checkout_page = CheckoutPage(context.driver)
    context.checkout_page.fill_checkout_information("Gloria", "Vicuña", "700001")
    context.checkout_page.click_continue()

@when('the user completes the purchase')
def step_user_clicks_finish(context):
    context.checkout_page = CheckoutPage(context.driver)
    context.checkout_page.click_finish()

@when('the item should be added to the cart')
def step_then_item_added_to_cart(context):
    context.inventory_page.go_to_cart()
    cart_items = context.driver.find_elements(By.CLASS_NAME, 'cart_item')
    assert len(cart_items) > 0, "No items found in the cart."

@then('the user should be redirected to the inventory page')
def step_then_inventory_page(context):
    assert context.inventory_page.is_inventory_page_displayed()

@then('an error message should be displayed')
def step_then_error_message(context):
    assert "Epic sadface" in context.login_page.get_error_message()


@then('the order should be completed successfully')
def step_order_completed(context):
    context.checkout_page = CheckoutPage(context.driver)
    assert context.checkout_page.is_order_complete(), "Order confirmation not found."
