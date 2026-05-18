import logging
from ui.web_element import WebElement
from ui.page_actions import PageActions
from utils.logger import LOGGER_NAME
from pages.base_page import BasePage

logger = logging.getLogger(LOGGER_NAME)


class WindowsNewPage(BasePage):

    def __init__(self, page):
        super().__init__(page)
        self.title = WebElement(
            locator=page.locator("//h3"),
            description='WindowsNewPage -> title',
            page=page
        )

    def get_title(self):
        return self.title.get_inner_text()
