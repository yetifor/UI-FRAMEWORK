from pages.basic_authorization_page import BasicAuthorizationPage
from utils.url_utils import embed_credentials_in_url
from utils.enums_data import DataEnum
from playwright.sync_api import Page


class TestBasicAuthorization:

    def test_basic_authorization(self,page):
        test_zone = embed_credentials_in_url(
            DataEnum.TEST_BY_BASIC_AUTH_URL,
            DataEnum.TEST_BY_BASIC_AUTH_USERNAME,
            DataEnum.TEST_BY_BASIC_AUTH_PASSWORD
            )
        page.goto(test_zone)
        authorization_page = BasicAuthorizationPage(page)
        result = authorization_page.get_expected_message()
        assert DataEnum.TEST_BY_BASIC_AUTH_EXPECTATIONS in result,(
            f'Test failed\n'
            f'Expected text {DataEnum.TEST_BY_BASIC_AUTH_EXPECTATIONS}\n'
            f'Actual text {result}')
