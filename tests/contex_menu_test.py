import logging
from pages.contex_menu_page import ContexEnums,ContexPage
from utils.logger import LOGGER_NAME

logger = logging.getLogger(LOGGER_NAME)


class TestContexMenu:

    def test_contex_menu(self, page):
        contex_page = ContexPage(page)
        contex_page.actions.goto(ContexEnums.URL)

        message = contex_page.actions.run_and_accept_alert(contex_page.right_click_hot_spot)
        assert message == ContexEnums.EXPECT_ALERT_TEXT,\
        f'Ожидалось сообщение: {ContexEnums.EXPECT_ALERT_TEXT}, получено: {message}'
