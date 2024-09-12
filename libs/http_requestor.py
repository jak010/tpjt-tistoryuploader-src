import requests


class HttpRequestProxy:

    @staticmethod
    def get(url):
        resp = requests.get(url)
        if resp.status_code == 200:
            return resp.text

        raise Exception("Http Request Failed")
