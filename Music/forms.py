from django import forms
from .models import Post_Music, Login_Data
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class LogInput (UserCreationForm):
      
      first_name = forms.CharField (max_length=30, widget = forms.TextInput(attrs={
         'class' : 'LogInput',
         'placeholder' : 'First Name',
         'autocomplate' : 'off'
      }))
      last_name = forms.CharField (max_length=30, widget = forms.TextInput(attrs={
         'class' : 'LogInput',
         'placeholder' : 'last Name',
         'autocomplate' : 'off'
      }))
      Email = forms.EmailField (widget = forms.EmailInput(attrs={
         'class' : 'LogInput',
         'placeholder' : 'Enter Email',
         'autocomplate' : 'off'
      }))
      password1 = forms.CharField (max_length=8, widget = forms.PasswordInput(attrs={
         'class' : 'LogInput',
         'placeholder' : 'Enter Password1',
         'autocomplate' : 'off'
      }))
      password2 = forms.CharField (max_length=8, widget = forms.PasswordInput(attrs={
         'class' : 'LogInput',
         'placeholder' : 'Enter Password2',
         'autocomplate' : 'off'
      }))
      
      class Meta:
          model = User
          fields = ('first_name', 'last_name', 'Email', 'password1', 'password2')

    # class Meta:

    #   model = Login_Data
    #   fields = 'first_name', 'last_name'


class Login_check (forms.Form):

  username = forms.CharField (widget = forms.TextInput(attrs={
    'class' : 'LogInput poppins-bold',
    'placeholder' : 'Enter Your Email'
    ''
  }))
  password = forms.CharField (widget = forms.TextInput(attrs={
    'class' : 'LogInput poppins-bold',
    'placeholder' : 'Password'
  }))