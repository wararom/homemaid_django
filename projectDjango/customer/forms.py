from django import forms
from django.forms import ModelForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.contrib.admin import widgets
import datetime
from .models import Maid, Reserve, Money, Customer
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ReserveForm(ModelForm):
    class Meta:
        model = Reserve
        exclude = ['user','image','cost','reseerve_date','maid_id']

    def __init__(self, *args, **kwargs):
        super(ReserveForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit','Reserve'))

class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        exclude = ['user']

    def __init__(self, *args, **kwargs):
        super(CustomerForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit','Register Now'))


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(max_length=254,)
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'password1', 'password2', 'email')
        exclude = []
        
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('__all__')
        exclude = ['user']

class UpSlipForm(forms.ModelForm):
    class Meta:
        model = Money
        exclude = ['resever_id','user']

    def __init__(self, *args, **kwargs):
        super(UpSlipForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit','Reserve Now'))
    
class MaidForm(forms.ModelForm):
    class Meta:
        model = Maid
        fields = ('__all__')