from django.forms import fields
from . import widgets
import country_list

class CharField(fields.CharField):
    widget = None
    def __init__(self, br=True, big=False, label='', attrs=None, **kwargs):
        self.br = br
        self.big = big
        self.label = label
        if big and self.widget == None:
            self.widget = widgets.TextArea(label, br, attrs)
        elif self.widget == None:
            self.widget = widgets.TextInput(label, br, attrs)
        else:
            self.widget = self.widget(label, br, attrs)

        kwargs['label'] = ''
        super().__init__(**kwargs)

class EmailField(CharField):
    widget = widgets.EmailInput

class SelectField(fields.ChoiceField):
    widget = None

    def __init__(self, choices, label='', attrs=None, **kwargs):
        self.widget = widgets.SelectInput(choices, label, attrs, **kwargs)
        kwargs['label'] = ''
        super().__init__(**kwargs)
        self.choices = choices

class captchaField(fields.FloatField):
    widget = widgets.HiddenInput

    def __init__(self, **kwargs):
        kwargs['label'] = ''
        super().__init__(**kwargs)

    def to_python(self, value):
        try:
            if float(value) > 1:
                return 1.0
            elif float(value) < 0:
                return 0.0
            else:
                return float(value)
        except ValueError:
            return None
