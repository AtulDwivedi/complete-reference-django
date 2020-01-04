from django.conf.urls import url
from . import views

app_name = 'items'

urlpatterns = [
    url(r"^$", views.ListItems.as_view(), name="all"),
    url(r"^(?P<pk>\d+)/", views.ItemDetail.as_view(), name="detail"),
]
