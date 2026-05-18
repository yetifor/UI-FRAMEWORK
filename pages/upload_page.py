import logging
import os
from pathlib import Path
from ui.web_element import WebElement
from playwright.sync_api import Page
from utils.logger import LOGGER_NAME
from ui.page_actions import PageActions
from pages.base_page import BasePage

logger = logging.getLogger(LOGGER_NAME)


class UploadPage(BasePage):

    def __init__(self, page):
        super().__init__(page)
        self.input_file = WebElement(
            locator=page.locator('#file-upload'),
            description='UploadPage -> input file',
            page=page,
        )
        self.upload_button = WebElement(
            locator=page.locator('#file-submit'),
            description='UploadPage -> upload button',
            page=page,
        )
        self.upload_text = WebElement(
            locator=page.locator('h3'),
            description='UploadPage -> upload text',
            page=page,
        )
        self.upload_file_name = WebElement(
            locator=page.locator('#uploaded-files'),
            description='UploadPage -> upload file name',
            page=page,
        )

    def upload_file(self, file_path):
        self.input_file.set_input_files(file_path)
        self.upload_button.click()

    def get_upload_text(self):
        return self.upload_text.get_inner_text()

    def get_upload_file_name(self):
        return self.upload_file_name.get_inner_text()
