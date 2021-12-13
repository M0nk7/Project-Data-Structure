from typing import List
from django.shortcuts import render,redirect
from .models import Post
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib.auth import logout

def home(request) :
    return render(request,'home.html')
def inHome(request) :
    return render(request,'inHome.html')
def signin(request) :
    return render(request,'signin.html')
def signinForm(request) :
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(
        password=password,
        username=username
        )
    if user is not None :
        login(request,user)
        return render(request,'inHome.html')
    else : return render(request,'signin.html')

def signup(request) :
    return render(request,'signup.html')
def signupForm(request):
    username = request.POST['username']
    firstname = request.POST['firstname']
    lastname = request.POST['lastname']
    email = request.POST['email']
    password = request.POST['password']
    rePassword = request.POST['rePassword']

    user = User.objects.create_user(
        password=password,
        username=username,
        first_name=firstname,
        last_name=lastname,
        email=email
    )
    user.save()

    return render(request,'signin.html')

def userLogout(request) :
    logout(request)
    return redirect('/')