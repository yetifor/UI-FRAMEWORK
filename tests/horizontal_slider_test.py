import logging
from pages.horizontal_slider_page import SliderPage, SliderEnums, SliderStrEnums
from utils.logger import LOGGER_NAME

logger = logging.getLogger(LOGGER_NAME)

class TestHorizontalSlider:

    def test_slider(self, page):
        slider1 = SliderPage(page)
        slider1.actions.goto(SliderStrEnums.URL)
        slider1.slider.click()
        val = slider1.generate_random_value(page)
        slider1.set_random_position_slider(val, page)
        slider1.page.wait_for_timeout(5000)
        assert float(slider1.slider_value.get_inner_text()) == val,\
        f'Актуальная позиция: {float(slider1.slider_value.get_inner_text())}, ожидаемая: {val}'