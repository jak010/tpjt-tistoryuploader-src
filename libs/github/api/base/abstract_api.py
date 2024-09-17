from functools import cached_property


class AbstractAPI:

    def __init__(self, user: str, repository: str, token: str):
        self.user = user
        self.repository = repository
        self.token = token

    @property
    def repo_dsn(self):
        return f"/{self.user}/{self.repository}"

    @cached_property
    def headers(self):
        request_headers = {}
        if self.token:
            request_headers["Authorization"] = f"token {self.token}"

        request_headers["Content-Type"] = "application/json"
        return request_headers
