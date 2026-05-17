import logging
from ui.multi_web_element import MultiWebElement
from ui.web_element import WebElement
from utils.logger import LOGGER_NAME
from ui.page_actions import PageActions

logger = logging.getLogger(LOGGER_NAME)

class ScrollPage:

    REQUIRED_QUANTITY= 10

    def __init__(self, page):
        self.page = page
        self.actions = PageActions(page)
        self.paragraphs = MultiWebElement(
            locator=page.locator("jscroll-added"),
            description='ScrollPage -> paragraphs',
            page=page,
        )

    def get_count_paragraphs(self):
        return self.paragraphs.count()

    def scrolling_page(self):
        logger.info('Scrolling page')
        self.page.evaluate("window.scrollTo(0, document.body.scrollHeight);")

    def scroll_to_paragraphs(self):
        counter = 0
        while counter < ScrollPage.REQUIRED_QUANTITY:
            self.get_count_paragraphs()
            counter += 1
            self.scrolling_page()

        return counter
