

class LoginPage:

    def __init__(self, page):
        self.page = page
        self._username = page.get_by_placeholder("Username")
        self._password = page.get_by_role("textbox", name="Password")
        self.login_btn = page.get_by_role("button", name="login")

    def navigate(self):
        self.page.goto("https://www.saucedemo.com/")

    def enter_username(self, u_name):
        self._username.clear()
        self._username.fill(u_name)

    def enter_password(self, password):
        self._password.clear()
        self._password.fill(password)

    def click_login(self):
        self.login_btn.click()

    def do_login(self):
        self.enter_username("standard_user")
        self.enter_password("secret_sauce")
        self.click_login()


