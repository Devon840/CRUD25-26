from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from django import forms
from django.forms.widgets import PasswordInput, TextInput
from .models import Record

# register and create a user
class CreateUserForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

# User login form
class LoginForm(AuthenticationForm):
    username = forms.CharField(widget = TextInput())
    password = forms.CharField(widget = PasswordInput())

<<<<<<< HEAD

class CreateRecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = ['first_name', 'last_name','email','phone','address','city']


class UpdateRecordsForm(forms.ModelForm):
    class meta:
        model = Record
        fields = ['first_name','last_name','email','phone','address','city']
=======
class CreateRecordForm(forms.ModelForm):
        class Meta:
             model = Record
             fields = ['first_name','last_name','email', 'phone','address','city']
>>>>>>> e7e30b9bf6e4833e8f25e46e9acad501b9714b39
