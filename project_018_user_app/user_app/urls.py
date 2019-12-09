from django.conf.urls import url
from . import views

app_name = 'user_app'

urlpatterns = [
    url(r'^index/', views.index, name='index'),
    url(r'^register/', views.user_registration, name='registration'),
    url(r'^user_login/', views.user_login, name='user_login'),
    url(r'^logout/', views.user_logout, name='logout'),
    url(r'^special/', views.special, name='special'),
]
