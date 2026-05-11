from enum import StrEnum

class DataEnum(StrEnum):
    TEST_BY_BASIC_AUTH_URL = 'http://the-internet.herokuapp.com/basic_auth'
    TEST_BY_BASIC_AUTH_USERNAME = 'admin'
    TEST_BY_BASIC_AUTH_PASSWORD = 'admin'
    TEST_BY_BASIC_AUTH_EXPECTATIONS = 'Congratulations! You must have the proper credentials.'