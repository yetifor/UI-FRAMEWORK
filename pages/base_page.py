import logging

from ui.page_actions import PageActions


class BasePage:

    def __init__(self, page):
        self.page = page
        self.actions = PageActions(page)