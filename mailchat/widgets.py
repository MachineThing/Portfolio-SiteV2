from django.forms.widgets import TextInput
from django.utils.safestring import mark_safe
from django.template import loader

class bTextInput(TextInput):
    template_name = 'widgets/TextInput.html'
    type = 'text'
    tag = 'input'

    def get_context(self, name, value, attrs):
        return {
            'widget': {
                'name': name,
                'is_hidden': self.is_hidden,
                'required': self.is_required,
                'value': self.format_value(value),
                'attrs': self.build_attrs(self.attrs, attrs),
                'template_name': self.template_name,
                'type' : self.type,
                'tag' : self.tag # Pretty sure this is heresy to HTML lovers but it does things quicker
            },
        }

class bTextArea(bTextInput):
    tag = 'textarea'

class bEmailInput(bTextInput):
    type = 'email'

class bHiddenInput(bTextInput):
    template_name = 'widgets/NoBrInput.html'
    type = 'hidden'
