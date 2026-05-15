import logging
from pages.frames_page import FramesPage,FramesText
from utils.logger import LOGGER_NAME

logger = logging.getLogger(LOGGER_NAME)

class TestFrames:


    def test_frame_page(self, page):
        page.goto(FramesText.URL)
        frame_page = FramesPage(page)
        left_text = frame_page.get_left_text()
        middle_text = frame_page.get_middle_text()
        right_text = frame_page.get_right_text()
        bottom_text = frame_page.get_bottom_text()
        assert left_text == FramesText.LEFT,\
            f'Ожидалось получить: {FramesText.LEFT}, получено: {left_text}'
        assert middle_text == FramesText.MIDDLE, \
            f'Ожидалось получить: {FramesText.MIDDLE}, получено: {middle_text}'
        assert right_text == FramesText.RIGHT, \
            f'Ожидалось получить: {FramesText.RIGHT}, получено: {right_text}'
        assert bottom_text == FramesText.BOTTOM,\
            f'Ожидалось получить: {FramesText.BOTTOM}, получено: {bottom_text}'


