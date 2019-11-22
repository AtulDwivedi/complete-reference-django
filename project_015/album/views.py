from django.shortcuts import render
from album.models import Photo
from album.forms import RegistrationForm

def index(request):
    dict = {'photos':Photo.objects.all()}
    return render(request, 'album/index.html', context=dict)

def registration_view(request):
    form = RegistrationForm()

    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            print('Naem: ' + form.cleaned_data['name'])
            print('Email: ' + form.cleaned_data['email'])
            print('Text: ' + form.cleaned_data['text'])
            return render(request, 'album/login.html', {})
    return render(request, 'album/registration.html', {'form': form})
