import logging
from pages.window_page import WindowsPage
from pages.windows_new_page import WindowsNewPage
from utils.logger import LOGGER_NAME




class TestWindows:
    EXCEPTION_TITLE = 'New Window'
    URL = 'https://the-internet.herokuapp.com/windows'

    def test_wind(self, page):
        main_wind = WindowsPage(page)
        main_wind.actions.goto(self.URL)
        new_page = main_wind.open_new_page()
        new_page.bring_to_front()
        new_page1 = WindowsNewPage(new_page)
        result = new_page1.get_title()
        assert result == self.EXCEPTION_TITLE, \
            f'Ожидался текст: {self.EXCEPTION_TITLE}, получен: {result}'

        main_wind.actions.bring_to_front()
        new_page = main_wind.open_new_page()
        new_page.bring_to_front()
        new_page2 = WindowsNewPage(new_page)
        result = new_page2.get_title()
        assert result == self.EXCEPTION_TITLE, \
            f'Ожидался текст: {self.EXCEPTION_TITLE}, получен: {result}'

        main_wind.actions.bring_to_front()
        new_page1.actions.close_page()
        new_page2.actions.close_page()
        res = page.context.pages
        assert len(res) == 1, \
            f'Ожидалось 1 открытая вкладка, получено: {len(res)}'
