from django.shortcuts import render

# Create your views here.
def index(request):
    msg_dict = {'success':"Everthing is successfull."}
    return render(request, 'first_app/index.html', context=msg_dict)
