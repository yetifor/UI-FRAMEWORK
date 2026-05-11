import logging
from playwright.sync_api import Page


class Browser:
    def __init__(self,page: Page):
        self.page = page

