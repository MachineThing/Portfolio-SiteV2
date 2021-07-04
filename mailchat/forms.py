from django.forms import Form
import country_list
from . import fields

class MailForm(Form):
    name = fields.CharField(label='Name:')
    company = fields.CharField(label='School/Company:')
    country = fields.SelectField(label='Country:', choices=tuple(country_list.countries_for_language('EN')))
    email = fields.EmailField(label='Email address:')
    subject = fields.CharField(label='Subject:')
    message = fields.CharField(min_length=100, big=True, label='Message:', attrs={'rows':3})
    # TODO: Make captcha_score actually get a recaptchaV3 score
    captcha_score = fields.captchaField(required=False)
