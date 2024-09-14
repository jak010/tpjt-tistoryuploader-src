import os

from dotenv import load_dotenv

from libs.github.github_api import GithubAPI
from libs.http_requestor import HttpRequestProxy
from libs.mkdown.parser import MarkDownParser
from libs.tistory.tistory_rss_parser import TistoryRssParser
from libs.tistory.tistory_uploader import TistoryUploader

load_dotenv()

gh = GithubAPI(
    user=os.environ['GH_ID'],
    repo_name=os.environ['GH_REPO']
)

latest_commit_sha = gh.repository.get_latest_commit_history()
addition_markdown_files = gh.repository.get_latest_commit_history_with_added_file_and_ext(
    sha=latest_commit_sha,
    file_ext="md"
)

markdowns = [
    MarkDownParser(
        HttpRequestProxy.get(addition_markdown_file.raw_url)
    )
    for addition_markdown_file in addition_markdown_files
]

# Write on Blog Post
tistory_rss_parser = TistoryRssParser(
    HttpRequestProxy.get(f"https://{os.environ['TISTORY_BLOG_DOMAIN']}.tistory.com/rss")
)

uploader = TistoryUploader(
    tsession=os.environ["TSESSION"],
    domain=os.environ["TISTORY_BLOG_DOMAIN"],
)

for markdown in tistory_rss_parser.uploadable_markdowns(markdown_parsers=markdowns):
    uploader.execute(
        title=markdown.get_markdown_title(),
        content=markdown.get_markdown_to_html
    )
