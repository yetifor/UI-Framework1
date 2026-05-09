from enum import StrEnum
from playwright.sync_api import Page
from ui.web_element import WebElement

class BasicAuthPage:
    def __init__(self, page: Page):
        self.page = page
        self.body = WebElement(page, 'body'


                               )