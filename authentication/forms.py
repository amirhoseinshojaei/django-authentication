from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=255)

    class Meta:
        model = User
        fields = (
            'first_name','last_name','username', 'email', 'password1', 'password2'
        )


class PasswordResetRequest(forms.ModelForm):
    email = forms.EmailField(label='Email')

class ConfirmPassword(forms.ModelForm):
    new_password = forms.CharField(max_length=255)
    confirm_password = forms.CharField(max_length=255)