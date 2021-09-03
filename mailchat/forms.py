from datetime import datetime
from django.forms import Form
from django.utils.crypto import get_random_string
from unidecode import unidecode
import country_list
from . import fields
from .models import Email

def return_countries():
    countries = country_list.countries_for_language('EN')[:] # Copy the list to avoid modifying the master list
    filter_list = lambda my_list, target:my_list.index(list(filter(lambda iterable:target.upper() in iterable, my_list))[0]) # Find index to the target
    # Remove "troll" countries
    troll_countries = ['KP', 'AQ']
    for count in troll_countries:
        countries.pop(filter_list(countries, count))

    # Reverse sort (while treating diacritics as normal alphabet or it will go wrong)
    countries.sort(key=lambda x: unidecode(x[1]).upper(), reverse=True)

    # Add some countries to the front
    countries += [countries.pop(filter_list(countries, 'GB'))]
    countries += [countries.pop(filter_list(countries, 'US'))]
    countries.reverse()
    return countries

class MailForm(Form):
    name = fields.CharField(label='Name:')
    company = fields.CharField(label='School/Company:')
    country = fields.SelectField(label='Country:', choices=return_countries())
    email = fields.EmailField(label='Email address:')
    subject = fields.CharField(label='Subject:')
    message = fields.CharField(big=True, label='Message:', attrs={'rows':3})

    def save(self, captcha_score):
        data = self.cleaned_data
        model = Email()
        model.verified = False
        model.sendee = data['email']
        model.sending_date = datetime.now()
        if captcha_score > 1 or captcha_score < 0:
            model.captcha_score = 0.0 # Sets the captcha_score to 0 if the score is fishy
        else:
            model.captcha_score = round(captcha_score, 2)
        model.verify_url = get_random_string(15)
        model.message = """---Header Start---
Sendee: {}
Sending Date: {}
Company: {}
Name: {}
Country: {}
Captcha Score: {}
--- Header End ---

Subject: {}

{}
""".format(data['email'], model.sending_date, data['company'], data['name'], data['country'], model.captcha_score, data['subject'], data['message'])
        model.save()
        return model
