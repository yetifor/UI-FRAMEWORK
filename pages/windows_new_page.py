import logging
from ui.web_element import WebElement
from ui.page_actions import PageActions
from utils.logger import LOGGER_NAME

logger = logging.getLogger(LOGGER_NAME)


class WindowsNewPage:

    def __init__(self, page):
        self.page = page
        self.actions = PageActions(page)
        self.title = WebElement(
            locator=page.locator("//h3"),
            description='WindowsNewPage -> title',
            page=page
        )

    def get_title(self):
        return self.title.get_inner_text()
