from .api.repository_api import RepositoryApi


class GithubAPI:

    def __init__(self, user: str, repo_name: str):
        self._user = user
        self._repo_name = repo_name

    @property
    def repository(self) -> RepositoryApi:
        return RepositoryApi(
            user=self._user,
            repository=self._repo_name
        )
