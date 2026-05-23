import logging
from pages.horizontal_slider_page import SliderPage
from utils.logger import LOGGER_NAME




class TestHorizontalSlider:
    URL = 'https://the-internet.herokuapp.com/horizontal_slider'

    def test_slider(self, page):
        slider1 = SliderPage(page)
        slider1.actions.goto(TestHorizontalSlider.URL)
        slider1.slider.click()
        random_value = slider1.get_random_value()
        slider1.set_position(random_value)
        res = slider1.get_actual_value()
        assert res == random_value,\
            f'Актуальная позиция: {res}, ожидаемая: {random_value}'
