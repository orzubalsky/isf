from django import forms
from letters.models import Signature


class SignatureForm(forms.ModelForm):
    """
    """
    class Meta:
        model = Signature
        fields = ('comment', )
