from django.shortcuts import render
from album.models import *
from album.forms import RegistrationForm

def index(request):
    dict = {'photos':Photo.objects.all()}
    return render(request, 'album/index.html', context=dict)

def registration_view(request):
    form = RegistrationForm()

    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            print('Email: ' + form.cleaned_data['email'])
            description = form.cleaned_data['text']
            category = Category.objects.get(category_name='Nature')
            photo = Photo(category = category,
            name = name,
            url = 'https://www.marshallsindia.com/images/younique/nature/nature-cover-slider-6.jpg',
            description = description)
            photo.save()
            return render(request, 'album/login.html', {})
    return render(request, 'album/registration.html', {'form': form})
