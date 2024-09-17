from .api import GithubPrivateAPI, GithubPublicAPI
from .constant import RepositoryType


class GithubAPIFactory:
    def __init__(self,
                 github_user_name: str,
                 github_repository: str,
                 github_token: str,
                 repository_type: str
                 ):
        self._user_name = github_user_name
        self._repo_name = github_repository
        self._github_token = github_token
        self._repository_type = repository_type

    def get_instance(self):
        if self._repository_type == RepositoryType.PUBLIC:
            return GithubPublicAPI(
                user_name=self._user_name,
                repo_name=self._repo_name
            )
        if self._repository_type == RepositoryType.PRIVATE:
            return GithubPrivateAPI(
                user_name=self._user_name,
                repo_name=self._repo_name,
                github_token=self._github_token,
                repository_type=self._repository_type
            )
