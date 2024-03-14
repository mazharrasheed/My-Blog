from django.shortcuts import redirect, render

from .forms import Sign_Up

# Create your views here.

def index(request):

  data={}
  return render(request,'index.html',data)


def dashboard(request):

  data={}
  return render(request,'dashboard.html',data)


def sign_up(request):
  if request.method=="POST":
    form=Sign_Up(request.POST)

  else:
    form=Sign_Up()

  data={'form':form}
  return render(request,'signup.html',data)


def sign_in(request):

  data={}
  return render(request,'signin.html',data)

