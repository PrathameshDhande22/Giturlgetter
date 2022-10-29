import os
from dotenv import load_dotenv
system_name=os.getlogin()
PATH=str(f'C:\\Users\\{system_name}\\AppData\\Roaming\\Python\\Python39\\site-packages\\command_line')
try:
    load_dotenv(f"{PATH}\\config.env")
except Exception as e:
    print(e)
files = os.listdir(PATH)
if "config.env" not in files:
    TOKEN_INSERTED = False
else:
    TOKEN_INSERTED = True
URL = "https://github.com/PrathameshDhande22/Git-URL-Extractor-using-Python"
TOKEN=os.getenv("Token")
