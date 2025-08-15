from playwright.sync_api import Page,expect

class ProductPage:
    def __init__(self,page=Page):
        self.page=page
        self.title=page.locator("span.title")

    def verifyonpage(self):
        return self.title
