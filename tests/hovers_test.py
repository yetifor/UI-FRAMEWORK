import logging
from pages.hovers_page import HoverPage
from utils.logger import LOGGER_NAME

logger = logging.getLogger(LOGGER_NAME)
URL = 'https://the-internet.herokuapp.com/hovers'


class TestHoverPage:

    def test_hovers(self, page):
        hover_page = HoverPage(page)
        hover_page.actions.goto(URL)
        count = hover_page.get_count_users()
        for i in range(count):
            name = hover_page.get_names_and_hover(i)
            hover_page.page.wait_for_timeout(5000)
            assert name == f'name: user{i + 1}', \
                f'Ожидалось name: user{i + 1}, получено {name}'
