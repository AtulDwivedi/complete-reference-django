from django.shortcuts import render
from album.models import Photo
# Create your views here.
def index(request):
    dict = {'photo':Photo.objects.all()[0]}
    return render(request, 'album/index.html', context=dict)
