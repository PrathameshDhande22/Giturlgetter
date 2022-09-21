from tkinter import messagebox
from requests import ConnectionError
from github import Github,UnknownObjectException


class GTExtract(Github):
    def __init__(self):
        super().__init__()

    def isValidUser(self, name):
        try:
            self.username = self.get_user(name)
            return True
        except UnknownObjectException as ex:
            if ex.status == 404:
                return False
        except ConnectionError as c:
            messagebox.showerror('Internet Connection',"Please Connect to the Internet")
        

    @property
    def get_all_user_repos(self):
        try:
            return self.username.get_repos()
        except AttributeError as a:
            return False

    def geturl(self, reponame, uname):
        repo = f"{uname}/{reponame}"
        return self.get_repo(repo).clone_url
