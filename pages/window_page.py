import logging
from ui.web_element import WebElement
from ui.page_actions import PageActions
from utils.logger import LOGGER_NAME, setup_logger
from pages.windows_new_page import WindowsNewPage
from pages.base_page import BasePage

logger = setup_logger(LOGGER_NAME)


class WindowsPage(BasePage):

    def __init__(self, page):
        super().__init__(page)
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
