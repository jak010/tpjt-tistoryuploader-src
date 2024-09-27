import json

import requests


class SlackNotificator:
    __instance = None

    @classmethod
    def with_url(cls, url):
        if cls.__instance is None:
            cls.__instance = SlackNotificator(url)
            return cls.__instance
        return cls.__instance

    def __init__(self, url):
        self.url = url

    def get_instance(self):
        if self.__instance is None:
            raise Exception(f"{self.__class__.__name__} IS NOT INITIALIZED.. ")

        return self.__instance

    def send_to(self, message: str):
        r = requests.post(
            self.url,
            headers={
                'Content-Type': 'application/json'
            },
            data=json.dumps(
                {
                    "text": message
                }
            ),
        )
        if r.status_code == 200:
            print("[*] Send Slack")
