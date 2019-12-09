from django.shortcuts import render
from user_app.forms import UserForm, UserProfileForm


def index(request):
    dict = {'django': 'Django: The web framework for perfectionists with deadlines.'}
    return render(request, 'user_app/index.html', dict)


def user_registration(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            profile.save()

            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render(request, 'user_app/registration.html', {'user_form': user_form, 'profile_form': profile_form, 'registered': registered})


def user_login(request):
    return render(request, 'user_app/login.html', {})


def user_logout(request):
    return render(request, 'user_app/login.html', {})
