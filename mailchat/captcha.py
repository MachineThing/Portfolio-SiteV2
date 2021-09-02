from django.conf import settings
import requests

# Exception

class CaptchaError(Exception):
    pass

# Function

def captcha(response):
    parameters = {
        'secret':settings.RECAPTCHA_PRIVATE_KEY,
        'response':response
    }
    result_raw = requests.post('https://www.google.com/recaptcha/api/siteverify', data=parameters)
    result = result_raw.json() # https://developers.google.com/recaptcha/docs/verify#api-response

    if result['success']:
        return result['score']
    else:
        raise CaptchaError
