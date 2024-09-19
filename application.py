import os

import requests
from dotenv import load_dotenv

from adapter.github.github_adapter import (
    GithubAPIAdapter
)
from adapter.tistory.tistory_rss_parser import TistoryRss
from adapter.tistory.tistory_uploader import TistoryUploader
from libs.mkdown.parser import MarkDownContent

load_dotenv()


class Application:

    def __init__(
            self,
            github_api_adapater: GithubAPIAdapter,
            tistory_parser: TistoryRss,
            tistory_uploader: TistoryUploader
    ):
        self.github_api_adapater = github_api_adapater.get_version()
        self.tistory_parser = tistory_parser
        self.tistory_uploader = tistory_uploader

    def execute(self):
        addition_markdown_files = self.github_api_adapater.repository.get_latest_history_with_added_file_and_ext(
            sha=self.github_api_adapater.repository.get_latest_commit(),
            file_ext="md"
        )

        markdown_content = MarkDownContent(
            title=addition_markdown_files[0].get_file_name(),
            raw_url=addition_markdown_files[0].get_raw_url()
        )

        if self.tistory_parser.is_uploadable_markdown(title=markdown_content.get_title()):
            self.tistory_uploader.execute(
                title=markdown_content.get_title(),
                content=markdown_content.get_html()
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
        tistory_parser=TistoryRss(
            tistory_rss.text
        ),
        tistory_uploader=TistoryUploader(
            tsession=os.environ["TSESSION"],
            domain=os.environ["TISTORY_BLOG_DOMAIN"],
        )
    )
    app.execute()
