import logging
from utils.logger import LOGGER_NAME
from enum import StrEnum
from playwright.sync_api import Page
from ui.web_element import WebElement
from ui.page_actions import PageActions

logger = logging.getLogger(LOGGER_NAME)


class ContexEnums(StrEnum):
    URL = 'https://the-internet.herokuapp.com/context_menu'
    EXPECT_ALERT_TEXT= 'You selected a context menu'


class ContexPage:
    def __init__(self, page):
        self.page = page
        self.actions = PageActions(page)
        self.hot_spot = WebElement(
            self.page.locator("#hot-spot"),
            description='ContexPage -> hot_spot'
        )

    def right_click_hot_spot(self):
        logger.info("PageActions: right click hot spot")
        self.hot_spot.right_click()

