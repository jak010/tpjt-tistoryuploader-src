from .repository_public_api import RepositoryPublicApi


class GithubPublicAPI:

    def __init__(self, user_name: str, repo_name: str):
        self.user_name = user_name
        self.repo_name = repo_name

    @property
    def repository(self) -> RepositoryPublicApi:
        return RepositoryPublicApi(
            user=self.user_name,
            repository=self.repo_name
        )


