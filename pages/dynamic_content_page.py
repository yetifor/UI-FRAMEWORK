import logging
from utils.logger import LOGGER_NAME
from ui.page_actions import PageActions
from ui.multi_web_element import MultiWebElement
from ui.web_element import WebElement

logger = logging.getLogger(LOGGER_NAME)


class DynamicContentPage:
    MAX_ATTEMPT = 10

    def __init__(self, page):
        self.page = page
        self.actions = PageActions(page)
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
        box = self._get_src_images()
        set_box = set(box)
        if len(box) == len(set_box):
            return False
        else:
            return True

    def _reload(self):
        return self.page.reload()

    def seek_duplicates_v2(self):
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
