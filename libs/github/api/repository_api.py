import requests

from .dto.addition_file_dto import AdditionFileDto

from typing import List, Dict


class RepositoryApi:
    _base_url = "https://api.github.com/repos"

    def __init__(self, user, repository):
        self._repo_dsn = f"/{user}/{repository}"

    def get_commit_histories(self) -> List[Dict]:
        """ 최근 커밋 목록 읽기 """
        _suffix_url = "/commits"
        r = requests.get(self._base_url + self._repo_dsn + _suffix_url)

        if r.status_code != 200:
            r.raise_for_status()

        return r.json()

    def get_commit_history_by_sha(self, sha: str):
        """ 해시값을 기준으로 커밋 정보 조회 """
        _suffix_url = f"/commits/{sha}"

        response = requests.get(self._base_url + self._repo_dsn + _suffix_url)

        if response.status_code != 200:
            response.raise_for_status()

        return response.json()

    def get_latest_commit_history(self) -> str:
        """ 최근 커밋의 sha 조회 """
        return self.get_commit_histories()[0].get("sha")

    def get_latest_commit_history_with_added_file(self, sha: str) -> List[AdditionFileDto]:
        """ 최근 커밋을 기준으로 추가된 파일만 조회하기 """
        data = self.get_commit_history_by_sha(sha)

        result = []
        for file_meta in data['files']:
            if file_meta["status"] == "added":
                result.append(
                    AdditionFileDto(
                        file_name=file_meta['filename'],
                        raw_url=file_meta['raw_url']
                    )
                )

        return result

    def get_latest_commit_history_with_added_file_and_ext(self, sha: str, file_ext: str) -> List[AdditionFileDto]:
        """ 최근 커밋된 내역 중, 신규 추가 파일과 확장자를 기준으로 가져오기 """
        addition_file_dtos = self.get_latest_commit_history_with_added_file(sha)

        result = []
        for addition_file_dto in addition_file_dtos:
            if addition_file_dto.get_file_ext() == file_ext:
                result.append(addition_file_dto)

        return result
