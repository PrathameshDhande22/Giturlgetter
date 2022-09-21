import os
from dotenv import load_dotenv
try:
    load_dotenv("config.env")
except Exception as e:
    print(e)
files = os.listdir(os.getcwd())
if "config.env" not in files:
    TOKEN_INSERTED = False
else:
    TOKEN_INSERTED = True
ICON = "Images/icon.ico"
LOGO = "Images/logo.png"
SEARCH = "Images/search.png"
GITHUB_LOGO = "Images/github-logo.png"
URL = "https://github.com/PrathameshDhande22/Git-URL-Extractor-using-Python"
TOKEN=os.getenv("Token")
