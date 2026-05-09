from playwright.sync_api import Page

from ui.web_element import WebElement


class LoginPage:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.email_input = WebElement(
            self.page.locator("#email"),
            description="Login page -> Email input",
        )
        self.password_input = WebElement(
            self.page.locator("#password"),
            description="Login page -> Password input",
        )
        self.submit_button = WebElement(
            self.page.locator("#submit"),
            description="Login page -> Submit button",
        )

    def login(self, email: str, password: str) -> None:
        self.email_input.fill(email)
        self.password_input.fill(password)
        self.submit_button.click()
