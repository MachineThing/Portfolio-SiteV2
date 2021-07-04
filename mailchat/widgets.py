from django.forms.widgets import TextInput as DjangoInput

class TextInput(DjangoInput):
    template_name = 'widgets/TextInput.html'
    type = 'text'
    tag = 'input'
    options = None

    def __init__(self, label='', br=True, attrs=None, **kwargs):
        self.label = label
        if not hasattr(self, 'br'):
            self.br = br
        super().__init__(attrs)

    def get_context(self, name, value, attrs):
        return {
            'widget': {
                'name': name,
                'is_hidden': self.is_hidden,
                'required': self.is_required,
                'value': self.format_value(value),
                'attrs': self.build_attrs(self.attrs, attrs),
                'template_name': self.template_name,
                'label' : self.label,
                'type' : self.type,
                'tag' : self.tag, # Pretty sure this is heresy to HTML lovers but it does things quicker
                'br' : self.br,
                'options' : self.options
            },
        }

class TextArea(TextInput):
    tag = 'textarea'

class EmailInput(TextInput):
    type = 'email'

class SelectInput(TextInput):
    template_name = 'widgets/SelectInput.html'
    type = None
    tag = None

    def __init__(self, options, label='', attrs=None, **kwargs):
        self.options = []
        for option in options:
            self.options.append({'key':option[0], 'value':option[1]})
        super().__init__(label, attrs=attrs)

class HiddenInput(TextInput):
    type = 'hidden'
    br = False
