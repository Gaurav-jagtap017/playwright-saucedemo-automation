class CheckoutPage:
    def __init__(self, page):
        self.page =page
        self._title = page.locator(".title")
        self._first_name_input = page.locator("#first-name")
        self._last_name_input = page.locator("#last-name")
        self._postal_code_input = page.locator("#postal-code")
        self._cancel_button = page.locator("#cancel")  #common for all pages of checkout.
        self._continue_button = page.locator("#continue")

        self._payment_information= page.locator("//div[@data-test='payment-info-value']")
        self._shipping_information = page.locator("//div[@data-test='shipping-info-value']")
        self._item_total = page.locator(".summary_subtotal_label")
        self._item_total = page.locator(".summary_total_label")
        self._finish_checkout = page.locator("#finish")

        self._confirmation_text = page.locator(".complete-header")
        self._back_to_products = page.locator("#back-to-products")

    def page_title(self):
        return self._title.inner_text()

    def fill_information(self, user):
        self._first_name_input.fill(user.first_name)
        self._last_name_input.fill(user.last_name)
        self._postal_code_input.fill(user.postal_code)

    def continue_checkout(self):
        self._continue_button.click()

    def cancel_checkout(self):
        self._cancel_button.click()

    def finish_checkout(self):
        self._finish_checkout.click()

    def confirmation_text(self):
        return self._confirmation_text.inner_text()

    def back_to_products(self):
        self._back_to_products.click()


