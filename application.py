import datetime
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
from adapter.slack.slack_logger import SlackNotificator

load_dotenv()


class Application:

    def __init__(
            self,
            github_api_adapater: GithubAPIAdapter,
            tistory_oauth_executer: OauthLoginExecuter,
            tistory_parser: TistoryRss
    ):
        self.github_api_adapater = github_api_adapater.get_version()
        self.tistory_oauth_executer = tistory_oauth_executer
        self.tistory_parser = tistory_parser
        self.logger = SlackNotificator.with_url(url=os.environ["SLACK_WEB_HOOK_URL"])

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
            self.tistory_oauth_executer.execute(
                kakao_id=os.environ["KAKAO_ID"],
                kakao_pw=os.environ["KAKAO_PW"]
            )
            self.logger.send_to(message=f"[+][{datetime.datetime.now()}:TISOTRY COOKIE LOG]:\n {self.tistory_oauth_executer.get_tsession()}")
            self.logger.send_to(message=f"[+][{datetime.datetime.now()}:TISOTRY USERANGET LOG]:\n {self.tistory_oauth_executer.get_user_agent()}")

            TistoryUploader.execute(
                title=markdown_content.get_title(),
                content=markdown_content.get_html(),
                tssession=self.tistory_oauth_executer.get_tsession(),
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
                executable_path="/usr/local/bin/chromedriver",
                option=ChromeOption(
                    window_size_width=780,
                    window_size_height=620
                )
            )
        ),
        tistory_parser=TistoryRss(
            tistory_rss.text
        )
    )
    app.execute()
