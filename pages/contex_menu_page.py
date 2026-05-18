import logging
from utils.logger import LOGGER_NAME
from enum import StrEnum
from playwright.sync_api import Page
from ui.web_element import WebElement
from ui.page_actions import PageActions
from pages.base_page import BasePage

logger = logging.getLogger(LOGGER_NAME)





class ContexPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.hot_spot = WebElement(
            self.page.locator("#hot-spot"),
            description='ContexPage -> hot_spot'
        )

    def right_click_hot_spot(self):
        logger.info("PageActions: right click hot spot")
        self.hot_spot.right_click()

