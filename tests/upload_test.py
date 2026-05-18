import logging
from pages.upload_page import UploadPage
from utils.logger import LOGGER_NAME

logger = logging.getLogger(LOGGER_NAME)


class TestUploadPage:
    TEXT_UPLOAD = 'File Uploaded!'
    FILENAME = 'file.txt'

    URL = 'https://the-internet.herokuapp.com/upload'

    def test_upload_page(self, page):
        upload_page = UploadPage(page)
        upload_page.actions.goto(TestUploadPage.URL)
        upload_page.upload_file(self.FILENAME)
        text_upload = upload_page.get_upload_text()
        filename = upload_page.get_upload_file_name()
        assert text_upload == self.TEXT_UPLOAD, \
            f'Ожидалсятекст: {self.TEXT_UPLOAD}, был получен {text_upload}'
        assert filename == self.FILENAME, \
            f'Оджилось имя файла: {self.FILENAME}, было получено {filename}'
