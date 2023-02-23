from playwright.sync_api import sync_playwright
from playwright.sync_api import Page, expect
import time


def test_loginPage_standareduser(set_up_tear_down):
    page = set_up_tear_down
    page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_role("textbox", name="Password").fill("secret_sauce")
    page.get_by_role("button", name="login").click()
    time.sleep(6)

    products_header = page.locator("span.title")

    expect(products_header).to_have_text("Products")


# def test_login_invailduser(page: Page):
#     page.goto("https://www.saucedemo.com/")
#     page.get_by_placeholder("Username").fill("invalid_user")
#     page.get_by_role("textbox", name="Password").fill("secret_sauce")
#     page.get_by_role("button", name="login").click()
#     time.sleep(6)

#     expect_fail_message = "Username and password do not match any user in this service"
#     err_msg_loc = page.locator(
#         "//h3[contains(text(),'Epic sadface: Username and password do not match a')]")
