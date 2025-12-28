from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from utils.random_strategy import RandomStrategy

class CheckoutFlow:
    def __init__(self, page):
        self.page = page

    def complete_checkout(self, user):
        inventory = InventoryPage(self.page)
        cart = CartPage(self.page)
        checkout = CheckoutPage(self.page)

        products = inventory.get_all_products()
        selected = RandomStrategy(seed=99).pick_products(products, 3)
        for product in selected:
            print(product.name)
            inventory.add_item_to_cart(product)

        cart.open()
        assert len(cart.get_cart_items()) == 3

        cart.proceed_to_checkout()
        checkout.fill_information(user)
        checkout.continue_checkout()
        checkout.finish_checkout()

        return checkout.confirmation_text()


