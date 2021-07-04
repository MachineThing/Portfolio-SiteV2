from django.forms.widgets import TextInput as DjangoInput

class TextInput(DjangoInput):
    template_name = 'widgets/TextInput.html'
    type = 'text'
    tag = 'input'

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
                'br' : self.br
            },
        }

class TextArea(TextInput):
    tag = 'textarea'

class EmailInput(TextInput):
    type = 'email'

class HiddenInput(TextInput):
    type = 'hidden'
    br = False
