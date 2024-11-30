from django.shortcuts import render, redirect
from .forms import LogInput, Login_check
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages

# Create your views here.

def index (request):

  return render (request, 'index.html')


def login_Page (request):

  form = Login_check(request.POST or None)

  if request.method == 'POST':
    if form.is_valid():

      username = form.cleaned_data.get('username')
      password = form.cleaned_data.get('password')

      user = authenticate (request, username=username, password=password)

      if user is not None:
        login (request, user)
        return redirect ('index')
      
  context = {
    'form' : form
  }
  
  return render (request, 'login.html', context)


def sign_up (request):

  form = LogInput (request.POST or None)
  if request.method == 'POST':
    if form.is_valid():
      
      messages.success(request, 'Successfully Register !!')
      form.save()
      return redirect ('login_Page')

  return render (request, 'Sign_up.html')