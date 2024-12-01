from django import forms
from .models import Post_Music, Login_Data
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# class LogInput (UserCreationForm):
      
#       first_name = forms.CharField (max_length=30, widget = forms.TextInput(attrs={
#          'class' : 'form-control',
#          'placeholder' : 'First Name',
#          'autocomplate' : 'off'
#       }))
#       last_name = forms.CharField (max_length=30, widget = forms.TextInput(attrs={
#          'class' : 'form-control',
#          'placeholder' : 'last Name',
#          'autocomplate' : 'off'
#       }))
#       username = forms.CharField (widget = forms.TextInput(attrs={
#          'class' : 'form-control',
#          'placeholder' : 'Enter username',
#          'autocomplate' : 'off'
#       }))
#       Email_Part= forms.EmailField (widget = forms.EmailInput(attrs={
#          'class' : 'form-control',
#          'placeholder' : 'Enter Email',
#          'autocomplate' : 'off'
#       }))
#       password1 = forms.CharField (max_length=40, label='password', widget = forms.PasswordInput(attrs={
#          'class' : 'form-control',
#          'placeholder' : 'Enter Password1',
#          'autocomplete': 'off'
#       }))
#       password2 = forms.CharField( max_length=40, label='Confirm Password', widget=forms.PasswordInput(attrs={
#           'class' : 'form-control',
#           'placeholder' : 'Confirm Password',
#           'autocomplete': 'off'
#       }))
      
#       class Meta:
#           model = User
#           fields = ('first_name', 'last_name', 'username', 'Email_Part', 'password1', 'password2')

    # class Meta:

    #   model = Login_Data
    #   fields = 'first_name', 'last_name'


class LogSecInput (UserCreationForm):      
      
      first_name = forms.CharField (max_length=30, widget = forms.TextInput(attrs={
         'class' : 'form-control',
         'placeholder' : 'First Name',
         'autocomplate' : 'off'
      }))
      last_name = forms.CharField (max_length=30, widget = forms.TextInput(attrs={
         'class' : 'form-control',
         'placeholder' : 'last Name',
         'autocomplate' : 'off'
      }))
      username = forms.CharField (widget = forms.TextInput(attrs={
         'class' : 'form-control',
         'placeholder' : 'Enter username',
         'autocomplate' : 'off'
      }))
      Email_Part= forms.EmailField (widget = forms.EmailInput(attrs={
         'class' : 'form-control',
         'placeholder' : 'Enter Email',
         'autocomplate' : 'off'
      }))
      password1 = forms.CharField (max_length=40, label='password', widget = forms.PasswordInput(attrs={
         'class' : 'form-control',
         'placeholder' : 'Enter Password1',
         'autocomplete': 'off'
      }))
      password2 = forms.CharField( max_length=40, label='Confirm Password', widget=forms.PasswordInput(attrs={
          'class' : 'form-control',
          'placeholder' : 'Confirm Password',
          'autocomplete': 'off'
      }))
      
      class Meta:
          model = User
          fields = ('first_name', 'last_name', 'username', 'Email_Part', 'password1', 'password2')


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