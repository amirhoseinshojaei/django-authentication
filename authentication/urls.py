from django.urls import path
from .import views
from django.contrib.auth import views as auth_views


app_name = 'authentication'

urlpatterns = [
    path("",views.home,name='home'),
    path("signup/",views.signup,name='signup'),
    path("login/",views.login,name='login'),
    path("password_change/",auth_views.PasswordChangeView.as_view(),name="password_change"),
    path("password_change/done/",auth_views.PasswordChangeDoneView.as_view(),name="password_change_done"),

]