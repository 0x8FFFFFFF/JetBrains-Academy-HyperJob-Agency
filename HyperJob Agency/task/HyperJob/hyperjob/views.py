from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic import CreateView


def menu(request):
    return render(request, 'hyperjob/menu.html')


class MyLoginView(LoginView):
    form_class = AuthenticationForm
    redirect_authenticated_user = False
    template_name = 'hyperjob/login.html'


class MySignupView(CreateView):
    form_class = UserCreationForm
    success_url = '/login/'
    template_name = 'hyperjob/signup.html'
