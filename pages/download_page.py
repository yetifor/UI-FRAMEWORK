import logging
from ui.multi_web_element import MultiWebElement
from ui.page_actions import PageActions
from ui.web_element import WebElement
from utils.logger import LOGGER_NAME

logger = logging.getLogger(LOGGER_NAME)


class DownloadPage:
    INDEX = 3

    def __init__(self, page):
        self.page = page
        self.actions = PageActions(page)
        self.download_links = MultiWebElement(
            locator=page.locator('.example a'),
            description='DownloadPage -> links',
            page=page
        )

    def get_filename_by_index(self, index=INDEX):
        link = self.download_links.nth(index - 1)
        return link.get_inner_text()

    def pick_file(self, index=INDEX):
        return self.download_links.nth(index - 1).click()
