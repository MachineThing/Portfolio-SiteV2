from . import widgets
from django import forms

class MailForm(forms.Form):
    email = forms.EmailField(widget=widgets.bEmailInput)
    subject = forms.CharField(widget=widgets.bTextInput)
    message = forms.CharField(min_length=100, widget=widgets.bTextArea)
    # TODO: Make captcha_score actually get a recaptchaV3 score
    captcha_score = forms.FloatField(min_value=0, max_value=1, required=False, widget=widgets.bHiddenInput, label='')
