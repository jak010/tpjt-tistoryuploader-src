import requests


class TistoryUploader:

    def __init__(self, tsession: str, domain: str):
        self._upload_url = f"https://{domain}.tistory.com/manage/post.json"
        self._cookies = {
            "TSSESSION": tsession
        }

    @property
    def _headers(self):
        return {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36",
            "Referer": "https://jako-note.tistory.com/manage/newpost/?type=post&returnURL=%2Fmanage%2Fposts%2F",
            "Content-Type": "application/json;charset=UTF-8",
            "Sec-Fetch-Site": "same-origin",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Dest": "empty"
        }

    def execute(self, title: str, content: str = None):
        r = requests.post(
            self._upload_url,
            headers=self._headers,
            cookies=self._cookies,
            json=self._upload_content(title=title, content=content)
        )
        return r.text

    def _upload_content(self, title: str, content: str = None):
        return {
            "id": "0",
            "title": title,
            "content": content,
            "slogan": "",
            "visibility": 20,
            "category": 0,
            "tag": "",
            "published": 1,
            "password": "",
            "uselessMarginForEntry": 2,
            "cclCommercial": 0,
            "cclDerive": 0,
            "thumbnail": None,
            "type": "post",
            "attachments": "",
            "recaptchaValue": "",
            "draftSequence": None
        }
