from playwright.sync_api import Locator

class Product:
    def __init__(self, name: str, price: float, root_locator: Locator):
        self.name = name
        self.price = price
        self.root_locator = root_locator

