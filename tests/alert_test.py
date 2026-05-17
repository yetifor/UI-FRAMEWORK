from pages.js_alerts_page import JsAlertsPage, AlertsEnums
from ui.page_actions import PageActions
from enum import StrEnum
from playwright.sync_api import Page
from faker import Faker
import logging
from utils.logger import LOGGER_NAME

fake = Faker()
logger = logging.getLogger(LOGGER_NAME)


class TestsJsAlerts:

    def test_alerts(self, page):
        page_action = PageActions(page)
        alerts_page = JsAlertsPage(page)
        logger.info(f'Переход по ссылке {AlertsEnums.URL}')
        page.goto(AlertsEnums.URL)
        logger.info('Клик по кнопке \'Click for JS Alert\'')
        message = page_action.run_and_accept_alert(alerts_page.click_js_alert_button)
        assert message == AlertsEnums.JS_ALERT, \
            f'Ожидался текст:{AlertsEnums.JS_ALERT}, получен: {message}'
        result = alerts_page.get_result_text()
        assert result == AlertsEnums.JS_ALERT_RESULT, \
            f'Ожидался резултат: {AlertsEnums.JS_ALERT_RESULT}, получен: {result}'
        logger.info('Клик по кнопке \'Click for JS Confirm\'')
        message = page_action.run_and_accept_alert(alerts_page.click_js_confirm_button)
        assert message == AlertsEnums.JS_CONFIRM, \
            f'Ожидался текст: {AlertsEnums.JS_CONFIRM}, получен: {message}'
        result = alerts_page.get_result_text()
        assert result == AlertsEnums.JS_CONFIRM_RESULT, \
            f'Ожидался Результат: {AlertsEnums.JS_CONFIRM_RESULT}, получен: {result}'
        random_word = fake.word()
        logger.info(f'Сгенерировано слово:{random_word}')
        logger.info('Клик по кнопке \'Click for JS Prompt\'')
        message = page_action.run_and_accept_prompt(alerts_page.click_js_prompt_button, prompt_text=random_word)
        assert message == AlertsEnums.JS_PROMPT, \
            f'Ожидался текст: {AlertsEnums.JS_PROMPT}, получен:  {message}'
        result = alerts_page.get_result_text()
        assert result == AlertsEnums.JS_PROMPT_RESULT + random_word, \
            f'Ожидался результат: {AlertsEnums.JS_PROMPT_RESULT + random_word}, получен: {result}'
