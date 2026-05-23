from enum import StrEnum

class BasicAuthorizationEnums(StrEnum):
    TEST_BY_BASIC_AUTH_URL = 'http://the-internet.herokuapp.com/basic_auth'
    TEST_BY_BASIC_AUTH_USERNAME = 'admin'
    TEST_BY_BASIC_AUTH_PASSWORD = 'admin'
    TEST_BY_BASIC_AUTH_EXPECTATIONS = 'Congratulations! You must have the proper credentials.'

class AlertsEnums(StrEnum):
    JS_ALERT ='I am a JS Alert'
    JS_ALERT_RESULT = 'You successfully clicked an alert'
    JS_CONFIRM ='I am a JS Confirm'
    JS_CONFIRM_RESULT = 'You clicked: Ok'
    JS_PROMPT = 'I am a JS Prompt'
    JS_PROMPT_RESULT = 'You entered: '

