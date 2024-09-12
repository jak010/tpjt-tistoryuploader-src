from xml.etree import ElementTree


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
