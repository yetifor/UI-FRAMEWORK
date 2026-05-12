from pages.basic_authorization_page import BasicAuthorizationPage
from utils.url_utils import embed_credentials_in_url
from utils.enums_data import BasicAuthorizationEnums
from playwright.sync_api import Page


class TestBasicAuthorization:

    def test_basic_authorization(self,page):
        test_zone = embed_credentials_in_url(
            BasicAuthorizationEnums.TEST_BY_BASIC_AUTH_URL,
            BasicAuthorizationEnums.TEST_BY_BASIC_AUTH_USERNAME,
            BasicAuthorizationEnums.TEST_BY_BASIC_AUTH_PASSWORD
            )
        page.goto(test_zone)
        authorization_page = BasicAuthorizationPage(page)
        result = authorization_page.get_expected_message()
        assert BasicAuthorizationEnums.TEST_BY_BASIC_AUTH_EXPECTATIONS in result,(
            f'Test failed\n'
            f'Expected text {BasicAuthorizationEnums.TEST_BY_BASIC_AUTH_EXPECTATIONS}\n'
            f'Actual text {result}')
