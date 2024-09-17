import os

from dotenv import load_dotenv

from libs.github import (
    GithubAPIFactory,
    RepositoryType
)

from libs.mkdown.parser import MarkDownContent

from libs.http_requestor import HttpRequestProxy
from libs.tistory.tistory_rss_parser import TistoryRssParser

from libs.tistory.tistory_uploader import TistoryUploader

load_dotenv()


class Application:

    def __init__(
            self,
            github_api: GithubAPIFactory,
            tistory_parser: TistoryRssParser,
            tistory_uploader: TistoryUploader
    ):
        self.github_api = github_api.get_instance()
        self.tistory_parser = tistory_parser
        self.tistory_uploader = tistory_uploader

    def execute(self):
        addition_markdown_files = self.github_api.repository.get_latest_history_with_added_file_and_ext(
            sha=self.github_api.repository.get_latest_commit(),
            file_ext="md"
        )

        content = self.github_api.repository.get_file_content(
            addition_file_dto=addition_markdown_files[0]
        )

        validate_markdown_contents = self.tistory_parser.is_uploadable_markdown_content(markdown_content=MarkDownContent(content))

        self.tistory_uploader.execute(
            title=validate_markdown_contents.get_markdown_title(),
            content=validate_markdown_contents.get_markdown_to_html()
        )


if __name__ == '__main__':
    app = Application(
        github_api=GithubAPIFactory(
            github_user_name=os.environ['GH_ID'],
            github_repository=os.environ['GH_REPO'],
            github_token=os.environ['GH_TOKEN'],
            repository_type=RepositoryType.of(os.environ['GH_REPO_TYPE'])
        ),
        tistory_parser=TistoryRssParser(
            HttpRequestProxy.get(f"https://{os.environ['TISTORY_BLOG_DOMAIN']}.tistory.com/rss")
        ),
        tistory_uploader=TistoryUploader(
            tsession=os.environ["TSESSION"],
            domain=os.environ["TISTORY_BLOG_DOMAIN"],
        )
    )
    app.execute()
