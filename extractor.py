import config
from github import Github, GithubException, UnknownObjectException, BadCredentialsException


class GTExtract(Github):
    def __init__(self):
        super().__init__(config.TOKEN)

    def isValidUser(self, name):
        try:
            self.username = self.get_user(name)
            return True
        except UnknownObjectException as ex:
            if ex.status == 404:
                return False
        except BadCredentialsException as e:
            if e.status == 401:
                print("Token are not valid please create it")
                creater = config.TokenAcceptor()

    @property
    def get_all_user_repos(self):
        return self.username.get_repos()

    def geturl(self, reponame, uname):
        repo = f"{uname}/{reponame}"
        return self.get_repo(repo).clone_url
