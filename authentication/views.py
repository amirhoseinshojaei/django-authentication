from django.shortcuts import render, redirect
from .forms import SignupForm
# Create your views here.

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
