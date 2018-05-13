from django import forms
from django.forms import ModelForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.contrib.admin import widgets
import datetime
from .models import Maid
from django.contrib import admin



class MaidForm(ModelForm):
    class Meta:
        model = Maid
        exclude = []

    def __init__(self, *args, **kwargs):
        super(MaidForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit','Register'))

class ImageUploadForm(forms.Form):
    """Image upload form."""
    image = forms.ImageField()