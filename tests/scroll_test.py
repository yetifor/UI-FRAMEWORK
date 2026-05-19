import logging
from pages.scroll_page import ScrollPage
from utils.logger import LOGGER_NAME

logger = logging.getLogger(LOGGER_NAME)


class TestScrollPage:
    URL = 'https://the-internet.herokuapp.com/infinite_scroll'

    def test_scroll_page(self, page):
        scroll_page = ScrollPage(page)
        scroll_page.actions.goto(TestScrollPage.URL)


        test_result = scroll_page.scroll_to_paragraphs()
        assert test_result == ScrollPage.REQUIRED_QUANTITY, \
            f'Ожидалось: {ScrollPage.REQUIRED_QUANTITY}, получено: {test_result}'
