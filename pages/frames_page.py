import logging
from playwright.sync_api import Page
from ui.web_element import WebElement
from utils.logger import LOGGER_NAME
from ui.page_actions import PageActions
from enum import StrEnum
from pages.base_page import BasePage

logger = logging.getLogger(LOGGER_NAME)


class FramesText(StrEnum):
    LEFT = 'LEFT'
    MIDDLE = 'MIDDLE'
    RIGHT = 'RIGHT'
    BOTTOM = 'BOTTOM'
    URL = 'https://the-internet.herokuapp.com/nested_frames'


class FramesPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.left_frame = WebElement(
            locator=page.frame(name="frame-left").locator("body"),
            description='FramesPage -> left frame',
            page=page
        )
        self.middle_frame = WebElement(
            locator=page.frame(name="frame-middle").locator('body'),
            description='FramesPage -> middle frame',
            page=page
        )
        self.right_frame = WebElement(
            locator=page.frame(name="frame-right").locator('body'),
            description='FramesPage -> right frame',
            page=page
        )
        self.bottom_frame = WebElement(
            locator=page.frame(name="frame-bottom").locator('body'),
            description='FramesPage -> bottom frame',
            page=page
        )

    def get_left_text(self):
        return self.left_frame.get_inner_text()

    def get_middle_text(self):
        return self.middle_frame.get_inner_text()

    def get_right_text(self):
        return self.right_frame.get_inner_text()

    def get_bottom_text(self):
        return self.bottom_frame.get_inner_text()
