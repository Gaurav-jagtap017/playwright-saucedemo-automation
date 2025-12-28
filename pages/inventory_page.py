from models.product import Product

class InventoryPage:
    def __init__(self, page):
        self.page = page
        self._title_locator= "span.title"
        self._product_common_locator= ".inventory_item"

    def get_title(self):
        return self.page.locator(self._title_locator).inner_text()
    def get_all_products(self):
        items = []
        list_product_locators  = self.page.locator(self._product_common_locator).all()
        total_products = len(list_product_locators)
        for item in list_product_locators:
            name = item.locator(".inventory_item_name").inner_text()
            price = float(item.locator(".inventory_item_price").inner_text().replace("$", ""))
            items.append(Product(name=name, price=price, root_locator=item))
        return items

    def add_item_to_cart(self, product:Product):
        product.root_locator.locator("button", has_text="Add to cart").click()