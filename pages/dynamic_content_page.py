import logging
from utils.logger import LOGGER_NAME
from ui.page_actions import PageActions
from ui.multi_web_element import MultiWebElement
from ui.web_element import WebElement
from pages.base_page import BasePage

logger = logging.getLogger(LOGGER_NAME)


class DynamicContentPage(BasePage):
    MAX_ATTEMPT = 10

    def __init__(self, page):
        super().__init__(page)
        self.images = MultiWebElement(
            locator=page.locator('img'),
            description='DynamicContentPage -> images',
            page=page
        )

    def _get_src_images(self):
        logger.info("DynamicContentPage: _get_src_images")
        box = []
        for image in self.images:
            image_src = image.get_attribute('src')
            box.append(image_src)
        return box

    def check_duplicates(self):
        logger.info("DynamicContentPage: check_duplicates")
        return len(self._get_src_images()) != len(set(self._get_src_images()))

    def seek_duplicates(self):
        logger.info("DynamicContentPage: seek_duplicates")
        attempts = int(self.MAX_ATTEMPT)
        for i in range(int(self.MAX_ATTEMPT)):
            attempts -= 1
            if attempts > 0 and self.check_duplicates():
                return True
            if attempts <= 0:
                return False
            else:
                self.actions.reload_page()
