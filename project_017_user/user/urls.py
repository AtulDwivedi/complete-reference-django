from django.conf.urls import url
from user import views

urlpatterns =[
    url(r'^$', views.index, name = 'index'),
    url(r'^index/', views.index, name = 'index'),
    url(r'^register/', views.registration, name = 'registration'),
    url(r'^login/', views.login, name = 'login'),
    url(r'^contact_us/', views.contact_us, name = 'contact_us'),
]
