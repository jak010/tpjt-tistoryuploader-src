from engine.driver import AbstractDriver
from engine.element import (
    KaKaoInputIdElement,
    KaKaoInputPasswordElement,
    KaKaoTistoryProfileElement,
    KaKaoLoginConfirmButtonElement
)
from oauth.login_requet import LoginRequest


class OauthLoginExecuter:

    def __init__(self, driver: AbstractDriver):
        self._driver: AbstractDriver = driver

    def execute(self, kakao_id: str, kakao_pw: str):
        login_request = LoginRequest()

        self._driver.move(login_request.execute())

        kakao_id = KaKaoInputIdElement(self._driver.get_instance()) \
            .input_element(value=kakao_id)

        kakao_pw = KaKaoInputPasswordElement(self._driver.get_instance()) \
            .input_element(value=kakao_pw)

        kakao_login_button = KaKaoLoginConfirmButtonElement(self._driver.get_instance()) \
            .click()

        kakao_tistory_prorifle = KaKaoTistoryProfileElement(self._driver.get_instance())

        return self._driver.get_cookies()
