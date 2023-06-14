from django import forms
from django.utils import timezone
from .models import *


class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ContactUsForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs = {'class': 'input-block', 'placeholder':'Nombre'}
        self.fields['email'].widget.attrs = {'class': 'input-block', 'placeholder':'Correo electrónico'}
        self.fields['phone'].widget.attrs = {'class': 'input-block', 'placeholder':'teléfono'}
        self.fields['message'].widget.attrs = {'class': 'input-block', 'placeholder':'Mensaje', "rows":"5"}
        self.fields['name'].label = False
        self.fields['email'].label = False
        self.fields['phone'].label = False
        self.fields['message'].label = False
