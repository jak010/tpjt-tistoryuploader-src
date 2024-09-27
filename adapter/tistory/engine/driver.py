from selenium.webdriver import Chrome
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.chrome.service import Service
from abc import ABCMeta, abstractmethod

from .options import AbstractOption


class AbstractDriver(metaclass=ABCMeta):
    _instance: WebDriver

    @classmethod
    @abstractmethod
    def build(cls, **kwars): ...

    @abstractmethod
    def get_instance(self): ...

    @abstractmethod
    def get_cookies(self): ...

    @abstractmethod
    def get_user_agent(self): ...

    @abstractmethod
    def move(self, url): ...


class ChromeDriver(AbstractDriver):
    _instance: WebDriver = None

    @classmethod
    def build(cls, executable_path: str = None, option: AbstractOption = None):
        if cls._instance is None:
            cls._instance = Chrome(
                service=Service(executable_path=executable_path),
                options=option.build() if option else None
            )
            return cls()
        return cls._instance

    def get_instance(self):
        return self._instance

    def get_cookies(self):
        return self._instance.get_cookies()

    def get_user_agent(self):
        return self.get_instance().execute_script("return navigator.userAgent")

    def move(self, url):
        self._instance.get(url)
