from core.base_page import BasePage
class LoginPage(BasePage):
    def login(self, username, password):
        self.page.goto("https://www.saucedemo.com/")
        self.fill("#user-name", username)
        self.fill("#password", password)
        self.click("#login-button")