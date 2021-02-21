from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Company, Profile

#Creating html forms.
# Each class interacts with a model. Fields for a form are chosen in 'fields'

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=False)
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(required=False)
    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['picture']

#this form doesn't directly interact with a model. fields are determined below
class CompanyUpdateForm(forms.Form):
    company = forms.ModelChoiceField(queryset=Company.objects.all(), required=False)
    key = forms.CharField(max_length=12, required=False)
    leave = forms.BooleanField(required=False, label='Check if you want to leave current company.')
