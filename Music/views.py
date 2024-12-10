from django.shortcuts import render, redirect
from .forms import LogInput, Login_check, postInput
from django.contrib.auth import (
  login, authenticate, logout
)
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Post_Music

# Create your views here.


@login_required (login_url='/login/')
def index (request):

  post_music = Post_Music.objects.all()

  context = {
    'post_music' : post_music
  }

  return render (request, 'index.html', context=context)



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


# def login_Page (request):
#   logout (request)
#   return redirect ('login_Page')


def sign_up (request):

  sign = LogInput (request.POST or None)
  if request.method == 'POST':
    if sign.is_valid():

      messages.success(request, 'Successfully Register !!')
      sign.save()
      return redirect ('login')
    

  context = {
    'sign' : sign
  }

  return render (request, 'Sign_up.html', context=context)


@login_required (login_url='/login/')
def post_page (request):

  postPage = postInput (request.POST or None)

  if request.method == 'POST':
    if postPage.is_valid():

      postPage.save()
      postPage = postInput()

  apply = Post_Music.objects.all()

  context = {
    'apply' : apply,
    'postPage' : postPage
  }

  return render (request, 'post_music.html', context=context)


def payment (request):

  # pay = specialKey (request.POST or None)

  # if request.method == 'POST':
  #   if pay.is_valid():
  #     if pay == '12345':

  #       return redirect ('index')
        # form.save()
        # form = specialKey ()

  # deploy = Spicalkey.objects.all()
  
  # context = {
  #   'pay' : pay,
  #   'deploy' : deploy
  # }

  return render (request, 'post_pay.html')