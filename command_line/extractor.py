from github import Github, UnknownObjectException
from .config import *
from typing import Generator
import requests


class GTExtract(Github):
    def __init__(self):
        super().__init__(TOKEN)

    @property
    def verifyname(self) -> bool:
        try:
            print(UNAME, TOKEN)
            name = self.get_user(UNAME)
            return True
        except UnknownObjectException:
            return False
        except requests.ConnectionError:
            return False

    def getlist(self, name) -> Generator:
        try:
            repo = self.get_user(name).get_repos()
            for r in repo:
                yield (r.id, r.full_name)
        except UnknownObjectException:
            return False
        except requests.ConnectionError:
            return False

    def getrepourl(self, value) -> list:
        try:
            clone_url = self.get_repo(value).clone_url
            url = self.get_repo(value).html_url
            ssh = self.get_repo(value).ssh_url
            git_url = self.get_repo(value).git_url
            return list(zip(["Clone Url", "Website Url", "SSH Url", "Git Url"], [clone_url, url, ssh, git_url]))
        except UnknownObjectException:
            return False
        except requests.ConnectionError:
            return False

    def details(self, user_name):
        try:
            details = self.get_user(user_name)
            list_op = ["User ID", "Name", "Bio", "Account Created On",
                       "Avatar URL", "Followers", "Following", "Email", "Website URL"]
            list_ret = [details.id, details.name, details.bio, details.created_at, details.avatar_url,
                        details.followers, details.following, details.email, details.html_url]
            return list(zip(list_op, list_ret))

        except UnknownObjectException:
            return None
        except requests.ConnectionError:
            return None
