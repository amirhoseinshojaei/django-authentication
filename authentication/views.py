from django.shortcuts import render, redirect
from .forms import SignupForm , PasswordResetRequest
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate , login 
from django.contrib.auth.models import User
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.template.loader import render_to_string
from django.core.mail import send_mail
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

def password_reset_request(request):

    if request.method=="POST":
        form = PasswordResetRequest(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get("email")
            try:
                user = User.objects.get(email = email)
            except user.DoesNotExist:
                user = None
            
            if user is not None:
                # Generate Toke & send email
                uid = urlsafe_base64_encode(force_bytes(user.pk))
                token = default_token_generator.make_token(user)
                password_reset_link = request.build_absolute_uri("/password_reset/confirm/"+uid+'/'+token+'/')
                email_subject = "Password Reset"
                email_body = render_to_string ('authentication/password_reset_email.html',{
                    'user':user,
                    'password_reset_link':password_reset_link
                })
                send_mail(email_subject,email_body,'from@example.com',[user.email])
                messages.success(request, 'An email has been sent with instructions to reset your password.')
                return redirect('password_reset_request')
            else:
                messages.error(request,"No user found with that email address")
    else:
        form = PasswordResetRequest()
    
    return render("authentication/password_reset_request.html",{'form':form})




