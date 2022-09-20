import os
from dotenv import load_dotenv
try:
    load_dotenv("config.env")
except Exception as e:
    print(e)


class TokenAcceptor():
    def __init__(self):
        self.token = input("Please Enter the Token : ")
        self.__createfile()

    def __createfile(self):
        with open("config.env", "w") as f:
            f.write(f"TOKEN={self.token}")


files = os.listdir(os.getcwd())
if "config.env" not in files:
    TOKEN_INSERTED = False
    obb = TokenAcceptor()
    TOKEN_INSERTED = True
else:
    TOKEN_INSERTED = True
ICON = "Images/icon.ico"
LOGO = "Images/logo.png"
SEARCH = "Images/search.png"
GITHUB_LOGO = "Images/github-logo.png"
URL = " "
TOKEN = os.getenv("Token")
