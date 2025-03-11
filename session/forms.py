from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.forms import Form
from .models import UserModel
from django.contrib.auth.models import User


class RegistrationForm(UserCreationForm):
    class Meta:
        model=User
        fields=('username','email','first_name','last_name')
class UserProfile(forms.ModelForm):
    bdate=forms.DateField(
        label='Birth Date',
        widget=forms.TextInput(
        attrs={'type':'date'}
    ))
    class Meta:
        model=UserModel
        #fields='__all__'
        exclude=('user',)
        labels={
            'bdate':'Birth Date',
        }