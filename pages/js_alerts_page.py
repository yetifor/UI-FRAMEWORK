import logging
from playwright.sync_api import Page
from faker import Faker

from ui.page_actions import PageActions
from utils.logger import LOGGER_NAME
from enum import StrEnum
from ui.web_element import WebElement
from ui.page_actions import PageActions

logger = logging.getLogger(LOGGER_NAME)


class AlertsEnums(StrEnum):
    URL = 'https://the-internet.herokuapp.com/javascript_alerts'
    JS_ALERT = 'I am a JS Alert'
    JS_ALERT_RESULT = 'You successfully clicked an alert'
    JS_CONFIRM = 'I am a JS Confirm'
    JS_CONFIRM_RESULT = 'You clicked: Ok'
    JS_PROMPT = 'I am a JS prompt'
    JS_PROMPT_RESULT = 'You entered: '


class JsAlertsPage:
    def __init__(self, page: Page):
        self.page = page
        self.js_alert_button = WebElement(
            self.page.get_by_role('button', name='Click for JS Alert'),
            description='JsAlertPage -> Alerts JS Button'
        )
        self.js_confirm_button = WebElement(
            self.page.get_by_role('button', name='Click for JS Confirm'),
            description='JsAlertPage -> Confirm JS Button'
        )
        self.js_prompt_button = WebElement(
            self.page.get_by_role('button', name='Click for JS Prompt'),
            description='JsAlertPage -> Prompt JS Button'
        )
        self.result = WebElement(
            self.page.locator("#result"),
            description='JsAlertPage -> Result JS Button'
        )

    def click_js_alert_button(self):
        logger.info('click js alert button')
        self.js_alert_button.click()

    def click_js_confirm_button(self):
        logger.info('click js confirm button')
        self.js_confirm_button.click()

    def click_js_prompt_button(self):
        logger.info('click js prompt button')
        self.js_prompt_button.click()

    def get_result_text(self):
        logger.info('Получил текст')
        return self.result.get_inner_text()
