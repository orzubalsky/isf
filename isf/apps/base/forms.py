from django.forms import *
from base.models import Person


class PersonForm(ModelForm):
    """
    """
    def __init__(self, *args, **kwargs):
        super(PersonForm, self).__init__(*args, **kwargs)

        self.fields['name'].error_messages['required'] = "Please enter your name"
        self.fields['email'].error_messages['required'] = "Please enter your email"

    class Meta:
        model = Person
        fields = ('name', 'email')
