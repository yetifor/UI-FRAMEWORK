import logging
from pydoc import describe

from  utils.logger import LOGGER_NAME
from playwright.sync_api import Page
from ui.page_actions import PageActions
from ui.web_element import WebElement
from ui.multi_web_element import MultiWebElement

logger = logging.getLogger(LOGGER_NAME)


class HoverPage:
    def __init__(self, page: Page):
        self.page = page
        self.actions = PageActions(page)
        self.image_element = WebElement(
            self.page.locator('.figure'),
            description= 'Hover Page -> image user'
        )
        self.image_elements = MultiWebElement(
            page = self.page,
            locator= self.page.locator('.figure'),
            description= "HoverPage -> images user",
        )



    def get_names_and_hover(self, index: int):
        logger.info('Get names and hover page')
        user = self.image_elements.nth(index)
        user.hover()
        name_user = WebElement(
            locator=user.locator.locator(".figcaption h5"),
            description='Hover Page -> name user',
            page = self.page)
        return name_user.get_inner_text()


    def get_count_users(self):
        logger.info('Get count users')
        return self.image_elements.count()

