import requests


class TistoryUploader:

    @staticmethod
    def execute(title: str, content: str = None, tssession: str = None, tistory_domain: str = None):
        r = requests.post(
            url=f"https://{tistory_domain}.tistory.com/manage/post.json",
            headers={
                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36",
                "Referer": f"https://{tistory_domain}.tistory.com/manage/newpost/?type=post&returnURL=%2Fmanage%2Fposts%2F",
                "Content-Type": "application/json;charset=UTF-8",
                "Sec-Fetch-Site": "same-origin",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Dest": "empty"
            },
            cookies={
                "TSSESSION": tssession
            },
            json={
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
        )
        return r.text
