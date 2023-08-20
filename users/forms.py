from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile 





class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'enter your email address here'}))
    

    class Meta:
        model = User #the model that'll be affected
        fields = ['username', 'email', 'password1','password2']
        widgets = {
            'username': forms.TextInput(attrs={'placeholder':'write your username here'}),
            'email':forms.TextInput(attrs={'placeholder':'enter your email address here'}),
            'password1':forms.PasswordInput(attrs={'placeholder':'enter a password'}),
            'password2':forms.PasswordInput(attrs={'placeholder':'confirm your password'}),
        }

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User #the model that'll be affected
        fields = ['username', 'email']