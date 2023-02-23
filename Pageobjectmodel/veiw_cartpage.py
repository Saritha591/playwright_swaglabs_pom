

class veiw_cartpage:

    def __init__(self, page):
        self.page = page
        self.veiw_cart = page.locator(" page.locator("//a[@class='shopping_cart_link']")")

    def view_cart(self):
        return self.view_cart