import markdown
import requests
from bs4 import BeautifulSoup


class MarkDownContent:

    def __init__(self, title, raw_url):
        self._title = title
        self._raw_url = raw_url

    def get_title(self) -> str:
        return self._title

    def get_header(self) -> str:
        soup = BeautifulSoup(self.get_html(), "html.parser")
        if soup.find("h1"):
            return soup.find("h1").text
        raise Exception("Html Header Tag is Not Found")

    def get_html(self) -> str:
        r = requests.get(self._raw_url)
        if r.status_code == 200:
            markdown_contents = markdown.markdown(
                r.text,
                extensions=[
                    "fenced_code",
                    "codehilite",
                    "smarty",
                    "toc"
                ]
            )
            return markdown_contents

        raise Exception("UnParsing")
