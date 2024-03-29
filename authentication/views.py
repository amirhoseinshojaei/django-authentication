from django.shortcuts import render, redirect
from .forms import SignupForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate , login
from django.contrib import messages
# Create your views here.

def home(request):
    return render (request,'home.html')

def signup(request):
    
    if request.method=='POST':
        signup_form = SignupForm(request.POST)
        if signup_form.is_valid:
            signup_form.save()
            return redirect('login')
    else:
        signup_form = SignupForm()
    context = {
        'form':signup_form
    }
    return render (request,'authentication/signup.html',context)

def login(request):

    if request.method == 'POST':
        login_form = AuthenticationForm(request,request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data.get("username")
            password = login_form.cleaned_data.get("password")
            user = authenticate(username=username , password=password)
            if user is not None:
                login(request,user)
                return redirect('home')
            else:
                messages.error(request,"Please first signup")
    else:
        login_form = AuthenticationForm()
    context = {
        'form':login_form
    }
    return render (request,"authentication/login.html",context)
