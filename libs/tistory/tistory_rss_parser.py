from typing import List
from xml.etree import ElementTree
from ..mkdown.parser import MarkDownParser
from functools import cached_property


class TistoryRssParser:

    def __init__(self, rss_xml):
        self.element = ElementTree.fromstring(rss_xml)

    def get_channels(self):
        return self.element.findall("./channel")

    @cached_property
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

    def uploadable_markdowns(self, markdown_parsers: List[MarkDownParser]) -> List[MarkDownParser]:
        result = []

        for rss_item in self.get_items:
            for markdown_parser in markdown_parsers:
                if markdown_parser.get_markdown_title() != rss_item['title']:
                    result.append(markdown_parser)
        return result
