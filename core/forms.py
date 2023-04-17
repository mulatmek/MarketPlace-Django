from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class LoginForm(AuthenticationForm):  
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Username',
        'class':'w-full px-5 py-1 text-gray-700 bg-gray-200 rounded focus:outline-none focus:bg-white'  
        }))
    
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Password',
        'class':'w-full px-5 py-1 text-gray-700 bg-gray-200 rounded focus:outline-none focus:bg-white'
        }))
    
class SignupForm (UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
    
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Username',
        'class':'w-full px-5 py-1 text-gray-700 bg-gray-200 rounded focus:outline-none focus:bg-white'  
        }))
    
    email = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Email',
        'class':'w-full px-5 py-1 text-gray-700 bg-gray-200 rounded focus:outline-none focus:bg-white'
        }))
    
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Password',
        'class':'w-full px-5 py-1 text-gray-700 bg-gray-200 rounded focus:outline-none focus:bg-white'
        }))
    
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Confirm Password',
        'class':'w-full px-5 py-1 text-gray-700 bg-gray-200 rounded focus:outline-none focus:bg-white'
        }))
    