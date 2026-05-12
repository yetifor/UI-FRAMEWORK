import logging
from playwright.sync_api import Page
from ui.page_actions import PageActions
from ui.web_element import WebElement
from utils.logger import LOGGER_NAME
from enum import Enum, StrEnum
from random import randint

logger = logging.getLogger(LOGGER_NAME)

class SliderEnums(Enum, StrEnum):
    URL = 'https://the-internet.herokuapp.com/horizontal_slider'
    MIN = 0.0
    MAX = 5.0
    STEP = 0.5

class SliderPage:
    def __init__(self, page: Page):
        self.page = page
        self.actions = PageActions(page)
        self.slider = WebElement(
            self.page.locator('input[value="range"]'),
            description= 'SliderPage -> slider'
        )

    def
