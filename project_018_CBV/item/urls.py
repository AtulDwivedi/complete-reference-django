from item import views
from django.conf.urls import url

app_name = 'item'

urlpatterns = [
    url(r'^index/', views.IndexView.as_view(), name = 'index'),
    url(r'^contact_us/', views.ContactUsView.as_view(), name = 'contact_us'),
    url(r'^about_us/', views.AboutUsView.as_view(), name = 'about_us'),
    url(r'^category/', views.CategoryListView.as_view(), name = 'category_list'),
    url(r'^categories/(?P<pk>\d+)/', views.CategoryDetailView.as_view(), name = 'category_detail'),
    url(r'^create/', views.CreateCategoryView.as_view(), name = 'category_create'),
    url(r'^update/(?P<pk>\d+)/', views.UpdateCategoryView.as_view(), name = 'category_update'),
    url(r'^delete/(?P<pk>\d+)/', views.DeleteCategoryView.as_view(), name = 'category_delete'),
]
