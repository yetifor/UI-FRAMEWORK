import logging
import random
from playwright.sync_api import Page
from ui.page_actions import PageActions
from ui.web_element import WebElement
from utils.logger import LOGGER_NAME
from enum import Enum, StrEnum
from pages.base_page import BasePage

logger = logging.getLogger(LOGGER_NAME)


class SliderEnums(Enum):
    MIN = 0.0
    MAX = 5.0
    STEP = 0.5


class SliderStrEnums(StrEnum):
    URL = 'https://the-internet.herokuapp.com/horizontal_slider'


class SliderPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.slider = WebElement(
            self.page.locator('input[type="range"]'),
            description='SliderPage -> slider'
        )
        self.slider_value = WebElement(
            self.page.locator('#range'),
            description='SliderPage -> slider range'
        )

    @staticmethod
    def generate_random_value(self):
        logger.info('Generate random value slider')
        values = [
            i * SliderEnums.STEP.value
            for i in range(int(SliderEnums.MAX.value / SliderEnums.STEP.value) + 1)]
        return random.choice(values)

    def set_random_position_slider(self, val, page: Page):
        logger.info('Random slider')
        x = 0
        while x == 0:
            if self._actual_value(page) < val:
                page.keyboard.press('ArrowRight')
            else:
                x += 1



    def _actual_value(self, page: Page):
        actual = self.slider_value.get_inner_text()
        return float(actual)
