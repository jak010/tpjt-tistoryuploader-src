import requests


class LoginRequest:
    url = "https://kauth.kakao.com/oauth/authorize"

    def __init__(self):
        self._headers = {
            "Host": "kauth.kakao.com",
            "Sec-Ch-Ua": '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
            "Sec-Ch-Ua-Mobile": "?0",
            "Sec-Ch-Ua-Platform": '"macOS"',
            "Upgrade-Insecure-Requests": "1",
            "Dnt": "1",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "Sec-Fetch-Site": "cross-site",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-User": "?1",
            "Sec-Fetch-Dest": "document",
            "Referer": "https://www.tistory.com/",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
            "Priority": "u=0, i",
            "Connection": "close",
            "X-Forwareded-For": "175.116.231.75"
        }

    def execute(self):
        resp = requests.get(
            self.url, params={
                "client_id": "3e6ddd834b023f24221217e370daed18",
                "state": "aHR0cHM6Ly93d3cudGlzdG9yeS5jb20v",
                "prompt": "select_account",
                "redirect_uri": "https://www.tistory.com/auth/kakao/redirect",
                "response_type": "code",
                "ka": "sdk/1.43.5 os/javascript sdk_type/javascript lang/ko-KR device/MacIntel origin/https%3A%2F%2Fwww.tistory.com",
                "is_popup": "false"
            },
            headers=self._headers,
            allow_redirects=False
        )
        if resp.status_code == 302:
            return resp.headers['Location']
        raise Exception(f"{self.__class__.__name__} execute faile")
