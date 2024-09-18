from .repository_public_api import RepositoryPublicApi
from ..dto.github_user_info import GithubUserInfo


class GithubPublicAPIEntry:

    def __init__(self, user_info: GithubUserInfo):
        self.user_info = user_info

    @property
    def repository(self) -> RepositoryPublicApi:
        return RepositoryPublicApi(
            user_info=self.user_info
        )
