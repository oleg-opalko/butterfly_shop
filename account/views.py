from django.contrib.auth import login, logout as auth_logout
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.views.generic import CreateView

from account.forms import UserLoginForm, UserRegisterForm


# Create your views here.

class UserLoginView(LoginView):
    form_class = UserLoginForm
    template_name = 'login.html'

    def get_success_url(self):
        return self.request.GET.get('next', '/')

class UserRegisterView(CreateView):
    form_class = UserRegisterForm
    template_name = 'register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('index')

def logout(request):
    auth_logout(request)
    return redirect('index')