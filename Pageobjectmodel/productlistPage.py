

class ProductlistPage:

    def __init__(self, page):
        self.page = page
        self.product_header = page.locator("span.title")

    def product_header(self):
        return self.product_header
        
