from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(max_length=20, label='Username', required=True, widget=forms.TextInput(attrs={'class': 'form-control',
                                                                                                             'placeholder': 'Username',
                                                                                                             'id': 'username',
                                                                                                             'data-rule': 'username',
                                                                                                             'data-msg': 'Please enter your username'}))
    email = forms.EmailField(max_length=50, label='Email', widget=forms.TextInput(attrs={'placeholder': 'Email',
                                                                                         'class': 'form-control',
                                                                                         'id': 'email',
                                                                                         'data-rule': 'email',
                                                                                         'data-msg': 'Please enter your email'}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'placeholder': 'Password',
                                                                                    'class': 'form-control',
                                                                                    'id': 'password1',
                                                                                    'data-rule': 'password',
                                                                                    'data-msg': 'Please enter your password'}))
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password',
                                                                                            'class': 'form-control',
                                                                                            'id': 'password2',
                                                                                            'data-rule': 'password',
                                                                             'data-msg': 'Please enter your password'}))
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(max_length=20, label='Username', required=True, widget=forms.TextInput(attrs={'class': 'form-control',
                                                                                                             'placeholder': 'Username',
                                                                                                             'id': 'username',
                                                                                                             'data-rule': 'username',
                                                                                                             'data-msg': 'Please enter your username'}))

    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'placeholder': 'Password',
                                                                                   'class': 'form-control',
                                                                                   'id': 'password',
                                                                                   'data-rule': 'password',
                                                                                   'data-msg': 'Please enter your password'}))