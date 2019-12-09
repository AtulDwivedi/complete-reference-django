from django.conf.urls import url
from . import views

app_name = 'user_app'

urlpatterns = [
    url(r'^index/', views.index, name='index'),
    url(r'^register/', views.user_registration, name='registration'),
    url(r'^login/', views.user_login, name='login'),
    url(r'^logout/', views.user_logout, name='logout'),
]
