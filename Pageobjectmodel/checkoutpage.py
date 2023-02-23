
class CheckoutPage:
    def __init__(self, page):
       self.page = page
       self.checkout_page = page.get_by_role("button", name="CHECKOUT")

    def checkout_page(self,page):
        return self.checkout_page
    
