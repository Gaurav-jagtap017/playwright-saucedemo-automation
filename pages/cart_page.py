class CartPage:
    def __init__(self, page):
        self.page =page
        self._cart_link = page.locator(".shopping_cart_link")
        self._cart_items = page.locator(".cart_item")
        self._checkout_button = page.locator("#checkout")
        self._continue_shopping = page.locator("#continue-shopping")

    def open(self):
        self._cart_link.click()

    def get_cart_items(self):
        return self._cart_items.all()

    def proceed_to_checkout(self):
        self._checkout_button.click()

    def continue_shopping(self):
        self._continue_shopping.click()

