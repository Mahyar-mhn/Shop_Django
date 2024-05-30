from django.shortcuts import render
from django.http import Http404, HttpResponse


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

    if request.method == 'POST':
        print(request.POST.get('Fullname'))
        print(request.POST.get('Email'))
        print(request.POST.get('Message'))

    context = {
        'contact': 'Welcome to contact us page'
    }
    return render(request, 'contact_us_page.html', context)
