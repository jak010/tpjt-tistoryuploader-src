from abc import ABCMeta, abstractmethod

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webdriver import WebDriver

from .driver import AbstractDriver

LOADING_TIME_LIMIT = 10


class AbstractElement(metaclass=ABCMeta):
    _element = None
    _element_type = None

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def element(self):
        element = WebDriverWait(self.driver, LOADING_TIME_LIMIT).until(
            ec.presence_of_element_located(
                (self._element_type, self._element)
            )
        )
        return element


class KaKaoInputIdElement(AbstractElement):
    """ KaKao Id 입력하기 """
    _element = "loginId"
    _element_type = By.NAME

    def input_element(self, value: str):
        element = self.element()
        element.send_keys(value)


class KaKaoInputPasswordElement(AbstractElement):
    """ KaKao Password Element """

    _element = "password"
    _element_type = By.NAME

    def input_element(self, value):
        element = self.element()
        element.send_keys(value)


class KaKaoLoginConfirmButtonElement(AbstractElement):
    """ KaKao Password Element """

    _element = '//*[@id="mainContent"]/div/div/form/div[4]/button[1]'  # 780x680
    _element_type = By.XPATH

    def click(self):
        element = self.element()
        element.click()


class KaKaoTistoryProfileElement(AbstractElement):
    """ KaKao/Tistory Profilx Box Element """
    _element = "inner_marticle_right"
    _element_type = By.CLASS_NAME
