from typing import List
from xml.etree import ElementTree
from ..mkdown.parser import MarkDownContent
from functools import cached_property


class TistoryRssParser:

    def __init__(self, rss_xml):
        self.element = ElementTree.fromstring(rss_xml)

    def get_channels(self):
        return self.element.findall("./channel")

    def get_items(self):
        """ Tisotry RSS 목록 리턴  """
        items = []
        for channel in self.get_channels():
            for item in channel.findall("item"):
                items.append(
                    {
                        "title": item.find("title").text,
                        "link": item.find("link").text
                    }
                )
        return items

    def is_uploadable_markdown_content(self, markdown_content: MarkDownContent) -> MarkDownContent:
        if not self.get_items():
            return markdown_content

        for rss_item in self.get_items():
            if markdown_content.get_markdown_title() != rss_item['title']:
                return markdown_content
