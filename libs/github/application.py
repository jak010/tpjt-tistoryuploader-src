from .api.repository_reader import RepositoryReader


class GithubAPI:

    def __init__(self, user: str, repo_name: str):
        self._user = user
        self._repo_name = repo_name

    @property
    def repository(self) -> RepositoryReader:
        return RepositoryReader(
            user=self._user,
            repository=self._repo_name
        )


if __name__ == '__main__':
    github_api = GithubAPI(user="jak010", repo_name="cyber-skills")

    latest_sha = github_api.repository.get_latest_sha_on_commit()

    data = github_api.repository.get_added_file_by_latest_commits(latest_sha)
    from pprint import pprint
    pprint(data)
