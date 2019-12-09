from django.shortcuts import render


def index(request):
    dict = {'django': 'Django: The web framework for perfectionists with deadlines.'}
    return render(request, 'user_app/index.html', dict)


def user_registration(request):
    return render(request, 'user_app/registration.html', {})


def user_login(request):
    return render(request, 'user_app/login.html', {})


def user_logout(request):
    return render(request, 'user_app/login.html', {})
