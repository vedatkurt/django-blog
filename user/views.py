from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages

from .forms import RegisterForm, LoginForm

def index(request):
    return render(request, "user/index.html")

def register(request):

    form = RegisterForm(request.POST or None)
    
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        #user = authenticate(username=username,password=password)
        #if user is None:
        newUser = User(username = username)
        newUser.set_password(password)
        newUser.save()

        login(request,newUser)

        messages.success(request,"You registered successfully!")
            
        return redirect("index")
        #else:
        #    messages.info(request,"Username/Password is wrong!")

    context = {
       "form" : form
    }
    return render(request, "user/register.html", context)

def loginUser(request):
    form = LoginForm(request.POST or None)

    context = {
       "form" : form
    }

    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        user = authenticate(username=username,password=password)

        if user is None:
            messages.info(request,"Username/Password is wrong!")
            return render(request, "user/login.html", context)
        else:
            messages.success(request,"Login successfully!")
            login(request,user)
            request.session['username'] = username
            messages.success(request,request.session['username'])
            return render(request, "index.html")
            #return redirect("index",user)

    return render(request, "user/login.html", context)

def logoutUser(request):
    logout(request)
    messages.success(request,"Logout successfully!")
    return redirect("index")

