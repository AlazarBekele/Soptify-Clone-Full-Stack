from django import forms
from .models import Post_Music, Login_Data

class LogInput (forms.ModelForm):
  class Meta:

    model = Login_Data
    fields = 'first_name', 'last_name'

    widgets = {
      'first_name' : forms.TextInput(attrs={
        'class' : ''
      }),
      'last_name' : forms.TextInput(attrs={
        'class' : 'LogInput poppins-bold'
      })
    }


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