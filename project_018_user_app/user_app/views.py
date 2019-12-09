from django.shortcuts import render


def index(request):
    return render(request, 'user_app/index.html', {})


def user_registration(request):
    return render(request, 'user_app/registration.html', {})


def user_login(request):
    return render(request, 'user_app/login.html', {})


def user_logout(request):
    return render(request, 'user_app/login.html', {})