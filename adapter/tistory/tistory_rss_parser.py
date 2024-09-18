from xml.etree import ElementTree


class TistoryRss:

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

    def is_uploadable_markdown(self, title: str) -> bool:
        if not self.get_items():
            return True

        if title not in [rss_item['title'] for rss_item in self.get_items()]:
            return True

        return False
