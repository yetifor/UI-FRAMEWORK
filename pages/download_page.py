import logging
from ui.multi_web_element import MultiWebElement
from ui.page_actions import PageActions
from ui.web_element import WebElement
from utils.logger import LOGGER_NAME
from pages.base_page import BasePage

logger = logging.getLogger(LOGGER_NAME)


class DownloadPage(BasePage):

    def __init__(self, page):
        super().__init__(page)
        self.download_links = MultiWebElement(
            locator=page.locator('.example a'),
            description='DownloadPage -> links',
            page=page
        )

    def get_filename_by_index(self, index):
        link = self.download_links.nth(index - 1)
        return link.get_inner_text()

    def pick_file(self, index):
        return self.download_links.nth(index - 1).click()
