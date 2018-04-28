from django import forms
from django.forms import ModelForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.contrib.admin import widgets
import datetime
from .models import Customer, Maid, Reserve, Money

class ReserveForm(ModelForm):
    class Meta:
        model = Reserve
        exclude = ['customer_id','image','cost']

    def __init__(self, *args, **kwargs):
        super(ReserveForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit','Reserve Now'))

class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        exclude = []

    def __init__(self, *args, **kwargs):
        super(CustomerForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit','Register Now'))

