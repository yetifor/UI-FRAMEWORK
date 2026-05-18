import logging
from utils.logger import LOGGER_NAME
from pages.basic_authorization_page import BasicAuthorizationPage
from utils.url_utils import embed_credentials_in_url
from utils.enums_data import BasicAuthorizationEnums

logger = logging.getLogger(LOGGER_NAME)


class TestBasicAuthorization:

    def test_basic_authorization(self, page):
        test_zone = embed_credentials_in_url(
            BasicAuthorizationEnums.TEST_BY_BASIC_AUTH_URL,
            BasicAuthorizationEnums.TEST_BY_BASIC_AUTH_USERNAME,
            BasicAuthorizationEnums.TEST_BY_BASIC_AUTH_PASSWORD
        )
        page.goto(test_zone)
        authorization_page = BasicAuthorizationPage(page)
        result = authorization_page.get_result_message()
        assert BasicAuthorizationEnums.TEST_BY_BASIC_AUTH_EXPECTATIONS in result, \
            f'Ожидалось: {BasicAuthorizationEnums.TEST_BY_BASIC_AUTH_EXPECTATIONS}, получено: {result}'
