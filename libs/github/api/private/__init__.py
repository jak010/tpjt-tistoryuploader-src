from .repositoy_private_api import RepositoryPrivateApi


class GithubPrivateAPI:
    def __init__(self, user_name: str, repo_name: str, github_token: str, repository_type: str):
        self.user_name = user_name
        self.repo_name = repo_name
        self.github_token = github_token
        self.repository_type = repository_type

    @property
    def repository(self) -> RepositoryPrivateApi:
        return RepositoryPrivateApi(
            user=self.user_name,
            repository=self.repo_name,
            github_token=self.github_token,
            repository_type=self.repository_type
        )
