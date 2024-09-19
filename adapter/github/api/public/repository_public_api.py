import base64
from typing import List, Dict

import requests

from ..base.abstract_api import AbstractAPI
from ..dto.addition_file_dto import AdditionFileDto
from ..dto.github_user_info import GithubUserInfo


class RepositoryPublicApi(AbstractAPI):
    _base_url = "https://api.github.com/repos"

    def __init__(self, user_info: GithubUserInfo):
        super().__init__(
            user_info=user_info
        )

    def get_commits(self) -> List[Dict]:
        """ 최근 커밋 목록 읽기 """
        _suffix_url = "/commits"

        r = requests.get(
            self._base_url + self.repo_dsn + _suffix_url,
            headers=self.headers
        )

        if r.status_code != 200:
            r.raise_for_status()

        return r.json()

    def get_commit_by_sha(self, sha: str):
        """ 해시값을 기준으로 커밋 정보 조회 """
        _suffix_url = f"/commits/{sha}"

        response = requests.get(
            self._base_url + self.repo_dsn + _suffix_url,
            headers=self.headers
        )

        if response.status_code != 200:
            response.raise_for_status()

        return response.json()

    def get_latest_commit(self) -> str:
        """ 최근 커밋의 sha 조회 """
        return self.get_commits()[0].get("sha")

    def get_addition_file_in_latest_commit(self, sha: str) -> List[AdditionFileDto]:
        """ 최근 커밋에서 Repository에 추가된 파일 조회하기 """
        data = self.get_commit_by_sha(sha)

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

    def get_latest_history_with_added_file_and_ext(self, sha: str, file_ext: str) -> List[AdditionFileDto]:
        """ 최근 커밋된 내역 중, 신규 추가 파일과 확장자를 기준으로 가져오기 """
        addition_file_dtos = self.get_addition_file_in_latest_commit(sha)

        result = []
        for addition_file_dto in addition_file_dtos:
            if addition_file_dto.get_file_ext() == file_ext:
                result.append(addition_file_dto)

        return result

    # def get_file_content(self, addition_file_dto: AdditionFileDto):
    #     resp = requests.get(addition_file_dto.raw_url)
    #     if resp.status_code == 200:
    #         return resp.text
    #
    #     resp.raise_for_status()
