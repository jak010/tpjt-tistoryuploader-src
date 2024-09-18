from .api.dto.github_user_info import GithubUserInfo
from .api import (
    GithubPrivateAPIEntry,
    GithubPublicAPIEntry
)

from .libs.enums.repository_type import RepositoryType


class GithubAPIAdapter:
    def __init__(self,
                 github_user_name: str,
                 github_repository: str,
                 github_token: str,
                 repository_type: str
                 ):
        self.user_info = GithubUserInfo(
            user_name=github_user_name,
            repo_name=github_repository,
            github_token=github_token,
            repository_type=RepositoryType.of(repository_type)
        )

    def get_version(self):
        if self.user_info.repository_type == RepositoryType.PUBLIC.value:
            return GithubPublicAPIEntry(
                user_info=self.user_info
            )
        if self.user_info.repository_type == RepositoryType.PRIVATE.value:
            return GithubPrivateAPIEntry(
                user_info=self.user_info,
            )
