from functools import cached_property
from ..dto.github_user_info import GithubUserInfo


class AbstractAPI:

    def __init__(self, user_info: GithubUserInfo):
        self.user_info = user_info

    @property
    def repo_dsn(self):
        return f"/{self.user_info.user_name}/{self.user_info.repo_name}"

    @cached_property
    def headers(self):
        request_headers = {}
        if self.user_info.github_token:
            request_headers["Authorization"] = f"token {self.user_info.github_token}"

        request_headers["Content-Type"] = "application/json"
        return request_headers
