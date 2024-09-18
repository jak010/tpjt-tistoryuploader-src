import dataclasses


@dataclasses.dataclass
class GithubUserInfo:
    user_name: str
    repo_name: str
    github_token: str
    repository_type: str
