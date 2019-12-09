from django.shortcuts import render
from user.forms import Registration, Login


def index(request):
    return render(request, 'user/index.html', {})


def registration(request):
    form = Registration()
    if request.method == 'POST':
        form = Registration(request.POST)
        if form.is_valid():
            print('Name: ' + form.cleaned_data['name'])
            print('experience: ' + str(form.cleaned_data['experience']))
            print('Email: ' + form.cleaned_data['email'])
            print('Password: ' + form.cleaned_data['password'])
            print('Form: ' + str(form.cleaned_data))
            return render(request, 'user/index.html', {'form': form})
        else:
            print(form.errors)
            return render(request, 'user/registration.html', {'form': form})
    else:
        return render(request, 'user/registration.html', {'form': form})


def login(request):
    form = Login()
    return render(request, 'user/login.html', {'form': form})


def contact_us(request):
    return render(request, 'user/contact_us.html', {})
