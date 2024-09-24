from abc import ABCMeta, abstractmethod

from selenium.webdriver import ChromeOptions


class AbstractOption(metaclass=ABCMeta):

    def __init__(self,
                 window_size_width: int,
                 window_size_height: int,
                 headless_allowed: bool = True,
                 sandbox_allowed: bool = True,
                 disable_gpu_allowed: bool = True,
                 disable_dev_shm_usage: bool = True
                 ):
        self.window_size_width = window_size_width
        self.window_size_height = window_size_height
        self.headless_allowed: bool = headless_allowed
        self.allowed_sandbox: bool = sandbox_allowed
        self.allowed_disable_gpu: bool = disable_gpu_allowed
        self.allowed_disable_dev_shm_usage: bool = disable_dev_shm_usage

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
        if self.headless_allowed:
            options.add_argument("--headless")
        if self.allowed_sandbox:
            options.add_argument("--no-sandbox")
        if self.allowed_disable_gpu:
            options.add_argument("--disable-gpu")
        if self.allowed_disable_dev_shm_usage:
            options.add_argument("--disable-dev-shm-usage")
        return options
