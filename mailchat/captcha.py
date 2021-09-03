from django.conf import settings
import requests

# Exception

class CaptchaError(Exception):
    pass

class CaptchaMissingSecret(CaptchaError):
    def __init__(self, message="The secret parameter is missing."):
        self.message = message
        super().__init__(self.message)

class CaptchaInvalidSecret(CaptchaError):
    def __init__(self, message="The secret parameter is invalid or malformed."):
        self.message = message
        super().__init__(self.message)

class CaptchaMissingResponse(CaptchaError):
    def __init__(self, message="The response parameter is missing."):
        self.message = message
        super().__init__(self.message)

class CaptchaInvalidResponse(CaptchaError):
    def __init__(self, message="The response parameter is invalid or malformed."):
        self.message = message
        super().__init__(self.message)

class CaptchaBadRequest(CaptchaError):
    def __init__(self, message="The request is invalid or malformed."):
        self.message = message
        super().__init__(self.message)

class CaptchaTimeout(CaptchaError):
    def __init__(self, message="The response is no longer valid: either is too old or has been used previously."):
        self.message = message
        super().__init__(self.message)

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
        try:
            if len(result['error-codes']) > 1:
                errors = ' & '.join(result['error-codes'])
                raise CaptchaError(errors)
            else:
                error_types = {'missing-input-secret':CaptchaMissingSecret,
                               'invalid-input-secret':CaptchaInvalidSecret,
                               'missing-input-response':CaptchaMissingResponse,
                               'invalid-input-response':CaptchaInvalidResponse,
                               'bad-request':CaptchaBadRequest,
                               'timeout-or-duplicate':CaptchaTimeout}
                try:
                    error_code = result['error-codes'][0]
                    raise error_types[error_code]
                except KeyError:
                    CaptchaError(f'Unknown error {error_code}')
        except KeyError:
            raise CaptchaError('Unknown error')
