import logging
from pages.download_page import DownloadPage
from utils.logger import LOGGER_NAME

logger = logging.getLogger(LOGGER_NAME)


class TestDownloadPage:
    URL = 'https://the-internet.herokuapp.com/download'

    def test_download_page(self, page):
        download_page = DownloadPage(page)
        download_page.actions.goto(self.URL)
        except_file = download_page.get_filename_by_index()
        with page.expect_download() as download_info:
            download_page.pick_file()
        download = download_info.value
        filename = download.suggested_filename
        assert except_file == filename, \
            f'Ожидалось имя: {filename}, было получено: {except_file}'
