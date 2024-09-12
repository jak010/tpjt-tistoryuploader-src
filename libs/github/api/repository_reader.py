import requests
from typing import List, Dict


class RepositoryReader:
    _base_url = "https://api.github.com/repos"

    def __init__(self, user, repository):
        self._repo_dsn = f"/{user}/{repository}"

    def get_commits(self) -> List[Dict]:
        _suffix_url = "/commits"
        r = requests.get(self._base_url + self._repo_dsn + _suffix_url)
        return r.json()

    def get_latest_sha_on_commit(self) -> str:
        """ 최근 커밋의 sha 조회 """
        _suffix_url = "/commits"

        response = requests.get(self._base_url + self._repo_dsn + _suffix_url)
        if response.status_code != 200:
            response.raise_for_status()

        return response.json()[0].get("sha")

    def get_commit_by_sha(self, sha: str):
        """ 해시값을 기준으로 커밋 정보 조회 """
        _suffix_url = f"/commits/{sha}"

        response = requests.get(self._base_url + self._repo_dsn + _suffix_url)
        if response.status_code != 200:
            response.raise_for_status()

        return response.json()

    def get_added_file_by_latest_commits(self, sha: str) -> List[Dict]:
        """ 최근 커밋을 기준으로 추가된 파일만 조회하기 """
        data = self.get_commit_by_sha(sha)

        result = []
        for file_meta in data['files']:
            if file_meta["status"] == "added":
                result.append(file_meta)

        return result
