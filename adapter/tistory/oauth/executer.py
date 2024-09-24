from .login_requet import LoginRequest
from ..engine.driver import AbstractDriver
from ..engine.element import (
    KaKaoInputIdElement,
    KaKaoInputPasswordElement,
    KaKaoTistoryProfileElement,
    KaKaoLoginConfirmButtonElement
)


class OauthLoginExecuter:

    def __init__(self, driver: AbstractDriver):
        self._driver: AbstractDriver = driver

    def execute(self, kakao_id: str, kakao_pw: str) -> dict:
        login_request = LoginRequest()

        self._driver.move(login_request.execute())

        kakao_input_id_element = KaKaoInputIdElement(self._driver.get_instance())
        kakao_input_id_element.execute(value=kakao_id)

        kakao_input_password_element = KaKaoInputPasswordElement(self._driver.get_instance())
        kakao_input_password_element.execute(value=kakao_pw)

        kakao_login_confirm_button_element = KaKaoLoginConfirmButtonElement(self._driver.get_instance())
        kakao_login_confirm_button_element.execute()

        kakao_tistory_pofile_element = KaKaoTistoryProfileElement(self._driver.get_instance())
        kakao_tistory_pofile_element.execute()

        return self._driver.get_cookies()
