class User:
    def __init__(self, login: str = "", password: str = "1041"):
        self.VipAccess = False
        self.username = login
        self.password = password

    def __str__(self) -> str:
        return f"{self.username} (pass: {self.password}, VIP: {self.VipAccess})"

    def login(self, *, resetpau: bool = False):
        if resetpau:
            self.username, self.password = input("Username -- "), input("Password -- ")
        self.VipAccess = input("VIP password -- ") == "5280"
        if not self.VipAccess:
            print("Incorrect.")
        else:
            print("Correct.")
