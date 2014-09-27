from django import forms
from events.models import Guest


class GuestForm(forms.ModelForm):
    """
    """
    class Meta:
        model = Guest
        fields = ('affiliation', 'proposal', )
