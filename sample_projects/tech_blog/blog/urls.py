from django.conf.urls import url
from blog import views

app_name = 'blog'

urlpatterns = [
    url(r'^$', views.PostListView.as_view(), name='post_list'),
    url(r'^about/$', views.AboutView.as_view(), name='blog_about'),
     url(r'^post/new/$', views.CreatePostView.as_view(), name='post_new'),
    url(r'^post/(?P<pk>\d+)$', views.PostDetailView.as_view(), name='post_detail'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.UpdatePostView.as_view(), name='post_edit'),
    url(r'^post/(?P<pk>\d+)/remove/$', views.DeletePostView.as_view(), name='post_remove'),
    url(r'^post/(?P<pk>\d+)/publish/$', views.publish_post, name='publish_post'),
    url(r'^post/(?P<pk>\d+)/comment/$', views.add_comment_to_post, name='add_comment_to_post'),
    url(r'^drafts/$', views.DrafPostView.as_view(), name = 'post_draft_list'),
    url(r'^comment/(?P<pk>\d+)/approve/$', views.approve_comment, name='approve_comment'),
    url(r'^comment/(?P<pk>\d+)/remove/$', views.remove_comment, name='remove_comment'),
]