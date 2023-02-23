from playwright.sync_api import sync_playwright
from playwright.sync_api import Page, expect
import time


def test_add_to_cart(set_up_tear_down):
    page = set_up_tear_down
    page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_role("textbox", name="Password").fill("secret_sauce")
    page.get_by_role("button", name="login").click()
    products_header = page.locator("span.title")
    expect(products_header).to_have_text("Products")

    product_name = "Sauce Labs Backbag"
    product_cart = page.locator(
        "//button[@id='add-to-cart-sauce-labs-backpack']")
    product_cart.click()
    time.sleep(4)
