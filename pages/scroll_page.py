import logging
from ui.multi_web_element import MultiWebElement
from ui.web_element import WebElement
from utils.logger import LOGGER_NAME
from ui.page_actions import PageActions
from pages.base_page import BasePage

logger = logging.getLogger(LOGGER_NAME)

class ScrollPage(BasePage):

    REQUIRED_QUANTITY= 10

    def __init__(self, page):
        super().__init__(page)
        self.paragraphs = MultiWebElement(
            locator=page.locator(".jscroll-added"),
            description='ScrollPage -> paragraphs',
            page=page,
        )

    def get_count_paragraphs(self):
        return self.paragraphs.count()

    def scroll_to_paragraphs(self, max_attempts: int = 60):
        for _ in range(max_attempts):
            count = self.get_count_paragraphs()
            logger.info(f"Прокрутка {_ + 1}: найдено {count} параграфов")
            if count >= self.REQUIRED_QUANTITY:
                return count
            self.paragraphs.last().scroll_into_view_if_needed()
            try:
                self.page.locator(".jscroll-added").nth(count - 1).wait_for(
                    state="attached",
                    timeout=10000
                )
            except RuntimeError:
                continue
        return self.get_count_paragraphs()
