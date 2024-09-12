import os

import requests
from dotenv import load_dotenv

from libs.github.application import GithubAPI
from libs.mkdown.parser import MarkDownParser
from libs.tistory.tistory_uploader import TistoryUploader
from libs.tistory.tistory_rss_parser import TistoryRssParser
from libs.http_requestor import HttpRequestProxy

load_dotenv()

gh = GithubAPI(
    user=os.environ['GH_ID'],
    repo_name=os.environ['GH_REPO']
)

sha = gh.repository.get_latest_sha_on_commit()
addition_files = gh.repository.get_added_file_by_latest_commits(sha)

#  Condition check

addtion_file_meta = []
if addition_files:
    for addition_file in addition_files:

        file_name = addition_file["filename"]
        save_dir, file_name = file_name.split("/")

        if addition_file['status'] == 'added':
            addtion_file_meta.append(
                {
                    "save_dir": save_dir,
                    "file_name": file_name,
                    "file_ext": file_name.split(".")[-1],
                    "raw_url": addition_file['raw_url']
                }
            )

# Write on Blog Post

for addtion_file in addtion_file_meta:

    if addtion_file['file_ext'] == 'md':
        markdown_parser = MarkDownParser(
            HttpRequestProxy.get(
                addtion_file['raw_url']
            )
        )

        tistory_rss_parser = TistoryRssParser(
            rss_xml=HttpRequestProxy.get(
                f"https://{os.environ['TISTORY_BLOG_DOMAIN']}.tistory.com/rss"
            )
        )

        for article in tistory_rss_parser.get_items():
            if markdown_parser.get_markdown_title() == article["title"]:
                print("Matched")

        # TistoryUploader(
        #     tsession=os.environ["TSESSION"],
        #     domain=os.environ["TISTORY_BLOG_DOMAIN"],
        # ).execute(
        #     title=markdown_parser.get_markdown_title(),
        #     content=markdown_parser.get_markdown_to_html
        # )
