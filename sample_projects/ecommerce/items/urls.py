from django.conf.urls import url
from . import views

app_name = 'items'

urlpatterns = [
    url(r"^$", views.ListItems.as_view(), name="all"),
]
