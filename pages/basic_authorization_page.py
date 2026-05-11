import logging
from utils.logger import LOGGER_NAME
from playwright.sync_api import Page
from ui.web_element import WebElement

logger = logging.getLogger(LOGGER_NAME)


class BasicAuthorizationPage:
    def __init__(self, page: Page):
        self.page = page
        self.expected_message = WebElement(
            self.page.locator('body'),
            description='Basic Authorization Page -> expected_message'
        )

    def get_expected_message(self):
        text = self.expected_message.get_text_content()
        logger.info(f'Expected message: {text}')
        return text


