from .repositoy_private_api import RepositoryPrivateApi
from ..dto.github_user_info import GithubUserInfo


class GithubPrivateAPIEntry:
    def __init__(self, user_info: GithubUserInfo):
        self.user_info = user_info

    @property
    def repository(self) -> RepositoryPrivateApi:
        return RepositoryPrivateApi(
            user_info=self.user_info
        )
