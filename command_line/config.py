from dotenv import load_dotenv, set_key
import os
import sys
import command_line

if sys.platform == "win32":
    PATH = command_line.__file__.replace("\__init__.py", "")
elif sys.platform == "linux":
    PATH = command_line.__file__.replace("/__init__.py", "")
else:
    print("Can't run on You System")
    sys.exit(0)

JSON_API = "$2b$10$IfzP7yV47A1YppQjMGTHIuvCJFQQLPaAusr60ru278afUqOeDnjkm"
BIN_ID = "6391b6fe6a51bc4f704a54f1"
all_paths = os.listdir(PATH)

if "config.env" not in all_paths:
    TOKEN_INSERTED = False
else:
    TOKEN_INSERTED = True
    load_dotenv(f"{PATH}/config.env")
    TOKEN = os.getenv("token")
    UNAME = os.getenv("uname")


def setvalue(name):
    set_key(f"{PATH}//config.env", key_to_set="uname", value_to_set=name)
