import markdown
from bs4 import BeautifulSoup


class MarkDownContent:

    def __init__(self, content):
        self.content = content

    def get_markdown_to_html(self) -> str:
        markdown_contents = markdown.markdown(
            self.content,
            extensions=[
                "fenced_code",
                "codehilite",
                "smarty",
                "toc"
            ]
        )
        return markdown_contents

    def get_markdown_title(self) -> str:
        soup = BeautifulSoup(self.get_markdown_to_html, "html.parser")
        if soup.find("h1"):
            return soup.find("h1").text

        raise Exception("Html Header Tag is Not Found")
