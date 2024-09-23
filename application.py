import os

import requests
from dotenv import load_dotenv

from adapter.github.github_adapter import (
    GithubAPIAdapter
)
from adapter.tistory.engine.driver import ChromeDriver
from adapter.tistory.engine.options import ChromeOption
from adapter.tistory.oauth.executer import OauthLoginExecuter
from adapter.tistory.rss.tistory_rss_parser import TistoryRss
from adapter.tistory.upload.tistory_uploader import TistoryUploader
from libs.mkdown.parser import MarkDownContent

load_dotenv()


class Application:

    def __init__(
            self,
            github_api_adapater: GithubAPIAdapter,
            tistory_oauth_executer: OauthLoginExecuter,
            tistory_parser: TistoryRss,
    ):
        self.github_api_adapater = github_api_adapater.get_version()

        self.tistory_oauth_executer = tistory_oauth_executer
        self.tistory_parser = tistory_parser

    def execute(self):
        addition_markdown_files = self.github_api_adapater.repository.get_latest_history_with_added_file_and_ext(
            sha=self.github_api_adapater.repository.get_latest_commit(),
            file_ext="md"
        )

        if not addition_markdown_files:
            raise Exception("Not Found Posting Contents")

        markdown_content = MarkDownContent(
            title=addition_markdown_files[0].get_file_name(),
            raw_url=addition_markdown_files[0].get_raw_url()
        )

        if self.tistory_parser.is_uploadable_markdown(title=markdown_content.get_title()):
            tistory_login_cookies = self.tistory_oauth_executer.execute(
                kakao_id=os.environ["KAKAO_ID"],
                kakao_pw=os.environ["KAKAO_PW"]
            )
            tssession = [cookie["value"] for cookie in tistory_login_cookies if cookie['name'] == 'TSSESSION'][0]

            TistoryUploader.execute(
                title=markdown_content.get_title(),
                content=markdown_content.get_html(),
                tssession=tssession,
                tistory_domain=os.environ['TISTORY_BLOG_DOMAIN']
            )


if __name__ == '__main__':
    tistory_rss = requests.get(f"https://{os.environ['TISTORY_BLOG_DOMAIN']}.tistory.com/rss")

    app = Application(
        github_api_adapater=GithubAPIAdapter(
            github_user_name=os.environ['GH_ID'],
            github_repository=os.environ['GH_REPO'],
            github_token=os.environ['GH_TOKEN'],
            repository_type=os.environ['GH_REPO_TYPE']
        ),
        tistory_oauth_executer=OauthLoginExecuter(
            driver=ChromeDriver.build(
                executable_path=None,
                option=ChromeOption(
                    window_size_width=720,
                    window_size_height=680
                )
            )
        ),
        tistory_parser=TistoryRss(
            tistory_rss.text
        )
    )
    app.execute()
