import logging

from utils.logger import LOGGER_NAME
from pages.dynamic_content_page import DynamicContentPage

logger = logging.getLogger(LOGGER_NAME)



class TestDynamic:

    URL = 'https://the-internet.herokuapp.com/dynamic_content'

    def test_dynamic_page(self, page):
        dynamic = DynamicContentPage(page)
        dynamic.actions.goto(self.URL)
        assert dynamic.seek_duplicates() == True
