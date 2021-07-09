from django.forms import Form
from unidecode import unidecode
import country_list
from . import fields

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
    message = fields.CharField(min_length=100, big=True, label='Message:', attrs={'rows':3})
    # TODO: Make captcha_score actually get a recaptchaV3 score
    captcha_score = fields.captchaField(required=False)
