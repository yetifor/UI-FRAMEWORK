import logging
from pages.contex_menu_page import  ContexPage
from utils.logger import LOGGER_NAME

logger = logging.getLogger(LOGGER_NAME)


class TestContexMenu:

    URL = 'https://the-internet.herokuapp.com/context_menu'
    EXPECT_ALERT_TEXT = 'You selected a context menu'

    def test_contex_menu(self, page):
        contex_page = ContexPage(page)
        contex_page.actions.goto(self.URL)

        message = contex_page.actions.run_and_accept_alert(contex_page.right_click_hot_spot)
        assert message == self.EXPECT_ALERT_TEXT, \
            f'Ожидалось сообщение: {self.EXPECT_ALERT_TEXT}, получено: {message}'
