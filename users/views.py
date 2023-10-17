from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth.views import LogoutView
from django.views.generic.base import TemplateView


# Create your views here.

class UserRegistrationView(CreateView):
    form_class = UserCreationForm
    template_name = 'register.html'
    success_url = reverse_lazy('users:login')

class UserLoginView(LoginView):
    template_name = 'login.html'


class CustomLogoutView(LogoutView):
    # Customize the logout behavior
    next_page = reverse_lazy('users:logged-out')  # Redirect to the home page for expenses

class CustomLogoutSuccessView(TemplateView):
    template_name = 'logged_out.html'

class HomeView(TemplateView):
    template_name = 'base.html'