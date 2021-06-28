from django import forms

class MailForm(forms.Form):
    email = forms.EmailField()
    subject = forms.CharField()
    message = forms.CharField(min_length=100)
    captcha_score = forms.FloatField(min_value=0, max_value=1)
