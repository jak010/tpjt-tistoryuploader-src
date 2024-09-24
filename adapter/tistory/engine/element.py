from abc import ABCMeta

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

ELEMENT_LOADING_WAIT_TIME_SECONDS = 30


class AbstractElement(metaclass=ABCMeta):
    _element = None
    _element_type = None

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def element(self):
        element = WebDriverWait(self.driver, ELEMENT_LOADING_WAIT_TIME_SECONDS).until(
            ec.presence_of_element_located(
                (self._element_type, self._element)
            )
        )
        return element


class KaKaoInputIdElement(AbstractElement):
    """ KaKao Id 입력하기 """
    _element = "loginId"
    _element_type = By.NAME

    def execute(self, value: str):
        element = self.element()
        element.send_keys(value)


class KaKaoInputPasswordElement(AbstractElement):
    """ KaKao Password Element """

    _element = "password"
    _element_type = By.NAME

    def execute(self, value):
        element = self.element()
        element.send_keys(value)


class KaKaoLoginConfirmButtonElement(AbstractElement):
    """ KaKao Password Element """

    _element = 'confirm_btn'  # 780x680
    _element_type = By.CLASS_NAME

    def execute(self):
        self.element().click()


class KaKaoTistoryProfileElement(AbstractElement):
    """ KaKao/Tistory Profilx Box Element """
    _element = "inner_marticle_right"
    _element_type = By.CLASS_NAME

    def execute(self):
        return self.element()
