from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model


class ContactForm(forms.Form):
    full_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your full name'})
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email address'})
    )
    message = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control'})
    )


class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your UserName'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter your Password'})
    )


User = get_user_model()


class RegisterForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your UserName'})
    )
    email = forms.EmailField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your EmailAddress'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter your Password'})
    )
    passwordConfirm = forms.CharField(
        label='Confirm Password',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm Password'})
    )

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise ValidationError('Username already exists')
        return username

    def clean_email(self):
        email = self.cleaned_data['email']

        if User.objects.filter(email=email).exists():
            raise ValidationError('Email already exists')

        return email

    def clean(self):
        data = self.cleaned_data
        password = self.cleaned_data.get('password')
        passwordConfirm = self.cleaned_data.get('passwordConfirm')
        if password != passwordConfirm:
            raise ValidationError('Passwords do not match')

        return data
