import logging
from utils.logger import LOGGER_NAME, setup_logger
from playwright.sync_api import Page
from ui.web_element import WebElement
from pages.base_page import BasePage

logger = setup_logger(LOGGER_NAME)


class BasicAuthorizationPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.result_message = WebElement(
            self.page.locator('body'),
            description='Basic Authorization Page -> expected_message'
        )

    def get_result_message(self):
        text = self.result_message.get_text_content()
        return text
