import logging
import random
from playwright.sync_api import Page
from ui.page_actions import PageActions
from ui.web_element import WebElement
from utils.logger import LOGGER_NAME, setup_logger
from enum import Enum, StrEnum
from pages.base_page import BasePage

logger = setup_logger(LOGGER_NAME)


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

    def get_min_value(self):
        min = self.slider.get_attribute('min')
        return float(min) if min else 0.0

    def get_max_value(self):
        max = self.slider.get_attribute('max')
        return float(max) if max else 5.0

    def get_step_value(self):
        step = self.slider.get_attribute('step')
        return float(step) if step else 0.5

    def get_actual_value(self):
        return float(self.slider_value.get_inner_text())

    def get_all_values(self):
        values = [
            i * self.get_step_value()
            for i in range(int(self.get_max_value() / self.get_step_value()) + 1)
        ]
        return values

    def get_random_value(self):
        return float(random.choice(self.get_all_values()))

    def set_position(self, value):
        random_value = value
        actual_value = self.get_actual_value()
        if actual_value == random_value:
            return
        if random_value > actual_value:
            key = 'ArrowRight'
            steps = (random_value - actual_value) / self.get_step_value()
        else:
            key = 'ArrowLeft'
            steps = (actual_value - random_value) / self.get_step_value()

        for i in range(int(steps)):
            self.slider.press(key)
