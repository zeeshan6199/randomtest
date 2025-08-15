from playwright.sync_api import Page,expect

class LoginPage:
    def __init__(self,page=Page):
        #hello
        self.page=page
        self.username=page.get_by_placeholder("Username")
        self.password=page.get_by_placeholder("Password")
        self.loginbtn=page.locator("input[type='submit']")

    def goto(self,url):
        self.page.goto(url)

    def loginaction(self,u,p):
        self.username.fill(u)
        self.password.fill(p)
        self.loginbtn.click()
