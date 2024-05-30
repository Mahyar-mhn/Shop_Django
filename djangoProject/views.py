from django.shortcuts import render, redirect
from django.http import Http404, HttpResponse
from .forms import *
from django.contrib.auth import authenticate, login, logout


def home_page(request):
    context = {
        'message': 'Hello World!'
                   ' this is sending data from context'
    }
    return render(request, 'home_page.html', context)


def about_page(request):
    context = {
        'about': 'About me'
    }
    return render(request, 'about_page.html', context)


def contact_page(request):
    contact_form = ContactForm()
    if request.method == 'POST':
        print(request.POST.get('Fullname'))
        print(request.POST.get('Email'))
        print(request.POST.get('Message'))

    context = {
        'contact': 'Welcome to contact us page',
        'contact_form': contact_form
    }
    return render(request, 'contact_us_page.html', context)


def login_page(request):
    print(request.user.is_authenticated)
    login_form = LoginForm(request.POST or None)
    if login_form.is_valid():
        username = login_form.cleaned_data.get('username')
        password = login_form.cleaned_data.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            print("Error")

    context = {
        'login': 'Welcome to Login page',
        'login_form': login_form
    }
    return render(request, 'auth/login_page.html', context)


def register_page(request):
    pass
