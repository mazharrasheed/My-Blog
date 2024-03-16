from django.contrib import messages
from django.contrib.auth import (authenticate, login, logout,
                                 update_session_auth_hash)
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render

from .forms import Add_Blog, Sign_Up
from .models import Blog

# Create your views here.

def index(request):
  if request.user.is_authenticated:
    myblog=Blog.objects.all()
  else:
    return redirect('signin')
  data={'myblog':myblog}
  return render(request,'index.html',data)


def dashboard(request):
  if request.user.is_authenticated:
    myblog=Blog.objects.all()

    if request.method=='POST':
      form=Add_Blog(request.POST)
      form.save()
    else:
      form=Add_Blog()
    data={'myblog':myblog,'form':form}
    return render(request,'dashboard.html',data)
  else:
    return redirect('signin')


def sign_up(request):
  if request.method=="POST":
    form=UserCreationForm(request.POST)
    if form.is_valid():
      form.save()
      messages.success(request,"account created succesfuly !!")
      return redirect('signup')
  else:
    form=UserCreationForm()

  data={'form':form}
  return render(request,'signup.html',data)

def log_out(request):

  logout(request)
  return redirect('signin')

def sign_in(request):
  mydata = {}
  if not request.user.is_authenticated:
    if request.method == 'POST':
      login_form = AuthenticationForm(request=request, data=request.POST)
      if login_form.is_valid():
        uname = login_form.cleaned_data['username']
        upass = login_form.cleaned_data['password']
        user = authenticate(username=uname, password=upass)
        if user is not None:
          login(request, user)
          messages.success(request, "You are successfuly login")
          return HttpResponseRedirect("/dashboard/")
    else:
      login_form = AuthenticationForm()
    
    mydata = {'form': login_form}
    return render(request, "signin.html", mydata)
  else:
    return redirect("dashboard")

  