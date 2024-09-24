from abc import ABCMeta, abstractmethod

from selenium.webdriver import ChromeOptions


class AbstractOption(metaclass=ABCMeta):

    def __init__(self,
                 window_size_width: int,
                 window_size_height: int,
                 allowed_headless: bool = True,
                 allowed_sandbox: bool = True,
                 allowed_disable_gpu: bool = True,
                 allowed_disable_dev_shm_usage: bool = True
                 ):
        self.window_size_width = window_size_width
        self.window_size_height = window_size_height
        self.allowed_headless: bool = allowed_headless
        self.allowed_sandbox: bool = allowed_sandbox
        self.allowed_disable_gpu: bool = allowed_disable_gpu
        self.allowed_disable_dev_shm_usage: bool = allowed_disable_dev_shm_usage

    @abstractmethod
    def build(self, **kwargs): ...


class ChromeOption(AbstractOption):
    _USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"

    def build(
            self,
    ) -> ChromeOptions:
        options = ChromeOptions()
        options.add_argument(
            "user-agent" + self._USER_AGENT,
        )
        options.add_argument(
            f"--window-size={self.window_size_width},{self.window_size_height}"
        )
        if self.allowed_headless:
            options.add_argument("--headless")
        if self.allowed_sandbox:
            options.add_argument("--no-sandbox")
        if self.allowed_disable_gpu:
            options.add_argument("--disable-gpu")
        if self.allowed_disable_dev_shm_usage:
            options.add_argument("--disable-dev-shm-usage")
        return options
