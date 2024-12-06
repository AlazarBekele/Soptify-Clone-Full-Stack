from django import forms
from .models import Post_Music, Login_Data
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class LogInput (UserCreationForm):
      
      first_name = forms.CharField (max_length=30, widget = forms.TextInput(attrs={
         'class' : 'form-control parkinsans',
         'placeholder' : 'First Name',
         'autocomplate' : 'off'
      }))
      last_name = forms.CharField (max_length=30, widget = forms.TextInput(attrs={
         'class' : 'form-control parkinsans',
         'placeholder' : 'last Name',
         'autocomplate' : 'off'
      }))
      username = forms.CharField (widget = forms.TextInput(attrs={
         'class' : 'form-control parkinsans',
         'placeholder' : 'Enter username',
         'autocomplate' : 'off'
      }))
      Email_Part= forms.EmailField (widget = forms.EmailInput(attrs={
         'class' : 'form-control parkinsans',
         'placeholder' : 'Enter Email',
         'autocomplate' : 'off'
      }))
      password1 = forms.CharField (max_length=40, label='password', widget = forms.PasswordInput(attrs={
         'class' : 'form-control parkinsans',
         'placeholder' : 'Enter Password1',
         'autocomplete': 'off'
      }))
      password2 = forms.CharField( max_length=40, label='Confirm Password', widget=forms.PasswordInput(attrs={
          'class' : 'form-control parkinsans',
          'placeholder' : 'Confirm Password',
          'autocomplete': 'off'
      }))
      
      class Meta:
          model = User
          fields = ('first_name', 'last_name', 'username', 'Email_Part', 'password1', 'password2')
          


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

  }))

  password = forms.CharField (widget = forms.TextInput(attrs={
      
    'class' : 'LogInput poppins-bold',
    'placeholder' : 'Password'

  }))


class postInput (forms.ModelForm):
    
    class Meta:
        
        model = Post_Music
        fields = '__all__'

        widgets = {
            
            'artist' : forms.TextInput(attrs={
                'class' : 'form-control bg-secondary text-light parkinsans',
                'placeholder' : 'Name Artist'
            }),
            'Music_Title' : forms.TextInput(attrs={
                'class' : 'form-control bg-secondary text-light parkinsans'
            }),
            'cover_picture' : forms.ClearableFileInput(attrs={
                'class' : 'form-control bg-secondary text-light parkinsans',
                'type' : 'file'
            }),
            'music' : forms.FileInput(attrs={
                'class' : 'form-control bg-secondary text-light parkinsans',
                'type' : 'file',
                'id' : 'formFileMultiple'
            }),
        }