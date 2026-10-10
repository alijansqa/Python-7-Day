class LoginPage:
    def __init__(self, pageName):    # constructor ( parameterized constructor
        self.page_name = pageName  # page is attribute
    def display(self):   # function
        print(self.page_name)
LoginPage = LoginPage("LoginPage")
print(LoginPage.display())