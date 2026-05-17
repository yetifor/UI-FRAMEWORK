import logging
from ui.web_element import WebElement
from ui.page_actions import PageActions
from utils.logger import LOGGER_NAME
from pages.windows_new_page import WindowsNewPage

logger = logging.getLogger(LOGGER_NAME)


class WindowsPage:

    def __init__(self, page):
        self.page = page
        self.actions = PageActions(page)
        self.click_here_link = WebElement(
            locator=page.get_by_role('link', name='Click Here'),
            description='WindowsPage -> click here link',
            page=page
        )

    def open_new_page(self):
        logger.info('Open new page')
        with self.page.context.expect_page() as new_page_info:
            self.click_here_link.click()
        return new_page_info.value
